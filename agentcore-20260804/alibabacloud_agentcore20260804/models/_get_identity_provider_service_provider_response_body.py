# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderServiceProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetIdentityProviderServiceProviderResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # If the request fails, handle the error based on the HTTP status code and the message.
        self.code = code
        # For the result structure, see the response fields of this operation. The response of an asynchronous write operation indicates that the request is accepted, but does not guarantee that the background task is completed.
        self.data = data
        # The processing status of the current request. This is not equivalent to the final result of the background task.
        self.http_status_code = http_status_code
        # The request acceptance or error message. For the result of an asynchronous task, check the corresponding query operation.
        self.message = message
        # The ID used to associate the current call with troubleshooting. Keep this ID if the request fails.
        self.request_id = request_id
        # A value of true indicates that the current request is processed successfully. For asynchronous writes, you must continue to query the task result.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetIdentityProviderServiceProviderResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetIdentityProviderServiceProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        acs_url: str = None,
        entity_id: str = None,
        metadata_xml: str = None,
        protocol: str = None,
    ):
        # The SAML assertion consumer service (ACS) URL of the SP. Configure this URL in the external IdP.
        self.acs_url = acs_url
        # The entity ID of the SP. Configure this ID in the external IdP. This is not the entity ID of the external IdP.
        self.entity_id = entity_id
        # The SP metadata XML for the external IdP to import. You cannot submit this XML as the IdP XML for SAML configuration.
        self.metadata_xml = metadata_xml
        # The query parameter is required and only supports the exact value SAML. The response returns SAML.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acs_url is not None:
            result['acsUrl'] = self.acs_url

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.metadata_xml is not None:
            result['metadataXml'] = self.metadata_xml

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acsUrl') is not None:
            self.acs_url = m.get('acsUrl')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('metadataXml') is not None:
            self.metadata_xml = m.get('metadataXml')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

