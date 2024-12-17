import requests
import xml.etree.ElementTree as ET

def call_web_service(url, headers, body):
    try:
        response = requests.post(url, headers=headers, data=body.encode('utf-8'),verify= False)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Falha na chamada {url}. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Erro: {str(e)}")
        return None

def compare_xml_responses(xml1, xml2):
    #  XMLs para objetos ElementTree
    try:
        root1 = ET.fromstring(xml1)
        root2 = ET.fromstring(xml2)
    except ET.ParseError as e:
        print(f"Error parsing XML: {str(e)}")
        return False
    
    # Compare os ElementTrees
    return ET.tostring(root1) == ET.tostring(root2)

def main():
    # URL, headers e body do primeiro serviço web
    url1 = "https://172.11717771.Web.Services.BKL.Tarifa/Tarifa"
    headers1 = {
        "Content-Type": "text/xml",
        "Authorization": "Bearer token1"
    }
    body1 = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tar="http://tarifa.webservice./">
   <soapenv:Header/>
   <soapenv:Body>
      <tar:estruturaConsultaTarifa>
         <dispositivoOrigem>
            <conteudoEnderecoIpOrigem>0000000</conteudoEnderecoIpOrigem>
            <identificadorDispositivoOrigem>00</identificadorDispositivoOrigem>
         </dispositivoOrigem>
         <autorizacao>
            <identificadorPontoAtendimento>88080889</identificadorPontoAtendimento>
            <dataAutorizacaoOrigem>20240722</dataAutorizacaoOrigem>
            <numeroAutorizacaoOrigem>0</numeroAutorizacaoOrigem>
            <identificadorCodigoTransacao>8888888</identificadorCodigoTransacao>
            <codigoCanalOrigem>null</codigoCanalOrigem>
         </autorizacao>
         <conta>
            <numeroAgencia>1</numeroAgencia>
            <numeroConta>8888888</numeroConta>
            <numeroVariacaoConta>0</numeroVariacaoConta>
            <indicadorTipoConta>1</indicadorTipoConta>
         </conta>
      </tar:estruturaConsultaTarifa>
   </soapenv:Body>
</soapenv:Envelope>
    """

    # URL, headers e body do segundo serviço web
    url2 = "https://177.1777.1777/Web.Services.Tarifa/Tarifa"
    headers2 = {
        "Content-Type": "text/xml",
        "Authorization": "Bearer token2",
        "Verify": "False"      
             
                 }
    body2 = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tar="http://tarifa.webservice.servidor.integracao.banklink.mb.foton.la/">
   <soapenv:Header/>
   <soapenv:Body>
      <tar:estruturaConsultaTarifa>
         <dispositivoOrigem>
            <conteudoEnderecoIpOrigem>172019000202028</conteudoEnderecoIpOrigem>
            <identificadorDispositivoOrigem>28</identificadorDispositivoOrigem>
         </dispositivoOrigem>
         <autorizacao>
            <identificadorPontoAtendimento>880009</identificadorPontoAtendimento>
            <dataAutorizacaoOrigem>20240722</dataAutorizacaoOrigem>
            <numeroAutorizacaoOrigem>0</numeroAutorizacaoOrigem>
            <identificadorCodigoTransacao>84023227</identificadorCodigoTransacao>
            <codigoCanalOrigem>null</codigoCanalOrigem>
         </autorizacao>
         <conta>
            <numeroAgencia>0</numeroAgencia>
            <numeroConta>0000</numeroConta>
            <numeroVariacaoConta>0</numeroVariacaoConta>
            <indicadorTipoConta>1</indicadorTipoConta>
         </conta>
      </tar:estruturaConsultaTarifa>
   </soapenv:Body>
</soapenv:Envelope>
    """
    
    # Chamada aos serviços web
    response1 = call_web_service(url1, headers1, body1)
    response2 = call_web_service(url2, headers2, body2)
    
    if response1 and response2:
        # Comparação das respostas XML
        if compare_xml_responses(response1, response2):
            print("As respostas dos serviços web são idênticas.")
        else:
            print("As respostas dos WS são diferentes.")
    else:
        print("Não foi possível obter respostas dos WS.")

if __name__ == "__main__":
    main()

