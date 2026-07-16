# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAtiRegistrantRequest(DaraModel):
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
        registrant_id: str = None,
        state: str = None,
        street: str = None,
    ):
        # The country.
        self.cc = cc
        # The city.
        self.city = city
        # Ensures the idempotency of the request. Generate a unique parameter value from your client to ensure that the value is unique across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters in length.
        # 
        # If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may be different for each API request.
        self.client_token = client_token
        # The document number of the registrant. Maximum length: 50 characters.
        self.document_code = document_code
        # The document image of the registrant (Base64-encoded). The original file size must be between 50 KB and 3 MB.
        self.document_image = document_image
        # The document type of the registrant. For more information, see the appendix on document types.
        self.document_type = document_type
        # The email address. Maximum length: 300 characters.
        self.email = email
        # The name of the registrant. Maximum length: 255 characters.
        self.name = name
        # The phone number of the registrant. Maximum length: 128 characters. If the country is China, the area code of a non-mobile phone number must match the city.
        self.phone = phone
        # The ID of the registrant profile.
        self.registrant_id = registrant_id
        # The state or province.
        self.state = state
        # The street.
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

        if self.registrant_id is not None:
            result['RegistrantId'] = self.registrant_id

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

        if m.get('RegistrantId') is not None:
            self.registrant_id = m.get('RegistrantId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Street') is not None:
            self.street = m.get('Street')

        return self

