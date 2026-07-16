# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAtiRegistrantRequest(DaraModel):
    def __init__(
        self,
        cc: str = None,
        city: str = None,
        client_token: str = None,
        document_code: str = None,
        document_image: str = None,
        document_type: str = None,
        email: str = None,
        name: str = None,
        phone: str = None,
        state: str = None,
        street: str = None,
    ):
        # The country or region of the registrant. Specify a 2-character country or region code in compliance with GB/T 2659.1-2022.
        # 
        # This parameter is required.
        self.cc = cc
        # The city of the registrant. The value cannot exceed 255 characters in length. If the country is China, the value must comply with GB/T 2260-2007.
        # 
        # This parameter is required.
        self.city = city
        # Ensures the idempotency of the request. Generate a unique parameter value from your client to ensure that the value is unique across different requests. The ClientToken value supports only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The document number of the registrant. The value cannot exceed 50 characters in length.
        # 
        # This parameter is required.
        self.document_code = document_code
        # The document image of the registrant in Base64 encoding. The original file size must be between 50 KB and 3 MB.
        # 
        # This parameter is required.
        self.document_image = document_image
        # The document type of the registrant.
        # | Field | Description             |
        # | ---- | ---------------- |
        # | SFZ   | ID card  |
        # | HZ    | Passport  |
        # | ORG   | Organization code certificate  |
        # | YYZZ	| Business license |
        # | BDDM | Military unit code |
        # | CHNSHXYD	| Unified Social Credit Code certificate of the People\\"s Republic of China |
        # | GAJMTX | Mainland Travel Permit for Hong Kong and Macao Residents |
        # | GAJZZ	| Residence Permit for Hong Kong and Macao Residents |
        # | GATLYCZD	| Registration certificate for permanent representative offices of tourism departments in Hong Kong, Macao, and Taiwan |
        # | GAXWZNDJ	| Registration certificate for permanent mainland journalist stations of Hong Kong and Macao news agencies |
        # | GZJGZY	| Notary office practice certificate |
        # | JDDWFW | Military unit paid service license |
        # | JGZ	| Military officer certificate |
        # | JJHFR	| Foundation legal person registration certificate |
        # | LSZY	| Law firm practice license |
        # | MBFQY	| Private non-enterprise unit registration certificate |
        # | MBXXBX	| Private school operating license |
        # | NCJTJJZZ	| Rural collective economic organization registration certificate |
        # | QTTYDM | Other - Unified Social Credit Code  |
        # | SFJD	| Judicial appraisal license |
        # | SHTTFR | Social organization legal person registration certificate |
        # | SHFWJG	| Social service institution registration certificate |
        # | SYDWFR | Public institution legal person certificate |
        # | TYDM  | Unified Social Credit Code certificate  |
        # | YLJGZY	| Medical institution practice license |
        # | ZCWYHDJZ	| Arbitration commission registration certificate |
        # | ZJCS	| Religious activity venue registration certificate |
        # | BJWSXX	| Beijing operating license for schools for children of foreign embassy staff |
        # | JWJG	| Overseas institution certificate |
        # | JWFZFDBJ	| Overseas non-governmental organization representative office registration certificate |
        # | WGCZJG | Foreign enterprise permanent representative office registration certificate |
        # | WGZHWH	| Foreign cultural center registration certificate in China |
        # | WGZHXWJG	| Foreign news agency certificate in China |
        # | WJLSFZ| Foreigner permanent residence ID card |
        # | WLCZJG	| Approval registration certificate for permanent representative offices of foreign government tourism departments |
        # | QT     | Other |
        # 
        # This parameter is required.
        self.document_type = document_type
        # The email address. The value cannot exceed 300 characters in length.
        # 
        # This parameter is required.
        self.email = email
        # The name of the registrant. The value cannot exceed 255 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The phone number of the registrant. The value cannot exceed 128 characters in length. If the country is China and the number is not a mobile phone number, the area code must match the city.
        # 
        # This parameter is required.
        self.phone = phone
        # The province of the registrant. The value cannot exceed 255 characters in length. If the country is China, the value must comply with GB/T 2260-2007.
        # 
        # This parameter is required.
        self.state = state
        # The address of the registrant. The value cannot exceed 255 characters in length.
        self.street = street

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cc is not None:
            result['Cc'] = self.cc

        if self.city is not None:
            result['City'] = self.city

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.document_code is not None:
            result['DocumentCode'] = self.document_code

        if self.document_image is not None:
            result['DocumentImage'] = self.document_image

        if self.document_type is not None:
            result['DocumentType'] = self.document_type

        if self.email is not None:
            result['Email'] = self.email

        if self.name is not None:
            result['Name'] = self.name

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.state is not None:
            result['State'] = self.state

        if self.street is not None:
            result['Street'] = self.street

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DocumentCode') is not None:
            self.document_code = m.get('DocumentCode')

        if m.get('DocumentImage') is not None:
            self.document_image = m.get('DocumentImage')

        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Street') is not None:
            self.street = m.get('Street')

        return self

