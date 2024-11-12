from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import telnetlib



def make_call(extension, phone_number):
    ami_host = settings.FREEPBX_AMI_HOST
    ami_port = settings.FREEPBX_AMI_PORT  # Typically 5038
    ami_user = settings.FREEPBX_AMI_USER
    ami_secret = settings.FREEPBX_AMI_SECRET

    try:
        tn = telnetlib.Telnet(ami_host, ami_port)
        tn.write(f"Action: Login\r\nUsername: {ami_user}\r\nSecret: {ami_secret}\r\n\r\n".encode('utf-8'))
        tn.write(f"Action: Originate\r\nChannel: SIP/{extension}\r\nContext: from-internal\r\nExten: {phone_number}\r\nPriority: 1\r\n\r\n".encode('utf-8'))
        response = tn.read_all().decode('utf-8')
        print(response)
        tn.close()
    except Exception as e:
        print(f"Error: {e}")
    
def softphone(request):
    make_call('92','0368989209')
    return render(request,'softphone.html')