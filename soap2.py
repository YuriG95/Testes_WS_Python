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
    #  XMLs para  ElementTree
    try:
        root1 = ET.fromstring(xml1)
        root2 = ET.fromstring(xml2)
    except ET.ParseError as e:
        print(f"Error parsing XML: {str(e)}")
        return False
    
    # Compare os ElementTrees
    return ET.tostring(root1) == ET.tostring(root2)

def main():
    # URL, headers e body do primeiro WS
    url1 = "https:************"
    headers1 = {
        "Content-Type": "text/xml",
        "Authorization": "Bearer token1"
    }
    body1 = """
<soapenv:Envelope xmlns:soapenv="http://******************.webservice./">
   <soapenv:Header/>
   <soapenv:Body>
      <tar:estttt>
         <dispositivoOrigem>
            <conteudoEnderecoIpOrigem>0000000</conteudoEnderecoIpOrigem>
            <identificadorDispositivoOrigem>00</identificadorDispositivoOrigem>
         </dispositivoOrigem>
         <autorizacao>
            <identificadorPontoAtendimento>00000000</identificadorPontoAtendimento>
            <dataAutorizacaoOrigem>20250722</dataAutorizacaoOrigem>
            <numeroAutorizacaoOrigem>0</numeroAutorizacaoOrigem>
            <identificadorCodigoTransacao>0000</identificadorCodigoTransacao>
            <codigoCanalOrigem>null</codigoCanalOrigem>
         </autorizacao>
         <conta>
            <numeroAgencia>1</numeroAgencia>
            <numeroConta>0000000000</numeroConta>
            <numeroVariacaoConta>0</numeroVariacaoConta>
            <indicadorTipoConta>0</indicadorTipoConta>
         </conta>
      </tar:estttt>
   </soapenv:Body>
</soapenv:Envelope>
    """

    # URL, headers e body do segundo WS
    url2 = "https:/************"
    headers2 = {
        "Content-Type": "text/xml",
        "Authorization": "Bearer token2",
        "Verify": "False"      
             
                 }
    body2 = """
<soapenv:Envelope xmlns:soapenv="http://******************.webservice./">
   <soapenv:Header/>
   <soapenv:Body>
      <tar:estttt>
         <dispositivoOrigem>
            <conteudoEnderecoIpOrigem>0000000</conteudoEnderecoIpOrigem>
            <identificadorDispositivoOrigem>00</identificadorDispositivoOrigem>
         </dispositivoOrigem>
         <autorizacao>
            <identificadorPontoAtendimento>00000000</identificadorPontoAtendimento>
            <dataAutorizacaoOrigem>20250722</dataAutorizacaoOrigem>
            <numeroAutorizacaoOrigem>0</numeroAutorizacaoOrigem>
            <identificadorCodigoTransacao>0000</identificadorCodigoTransacao>
            <codigoCanalOrigem>null</codigoCanalOrigem>
         </autorizacao>
         <conta>
            <numeroAgencia>1</numeroAgencia>
            <numeroConta>0000000000</numeroConta>
            <numeroVariacaoConta>0</numeroVariacaoConta>
            <indicadorTipoConta>0</indicadorTipoConta>
         </conta>
      </tar:estttt>
   </soapenv:Body>
</soapenv:Envelope>
    """
    
    # Chamada WS
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

