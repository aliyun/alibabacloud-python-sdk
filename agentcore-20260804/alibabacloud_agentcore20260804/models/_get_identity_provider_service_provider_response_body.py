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
        # The business result code. If the request fails, handle the error based on the HTTP status code and the message.
        self.code = code
        # The SP information. For the result structure, see the response fields of this operation. The response of an asynchronous write operation indicates that the request is accepted, which does not guarantee that the background task is complete.
        self.data = data
        # The processing status of the current request. This status is not equivalent to the final result of the background task.
        self.http_status_code = http_status_code
        # The message about request acceptance or errors. Check the asynchronous task result by calling the corresponding query operation.
        self.message = message
        # The ID of the request. You can use the ID to associate the call with troubleshooting. Keep the ID if the request fails.
        self.request_id = request_id
        # Indicates whether the current request is successful. A value of true indicates that the request is processed successfully. For asynchronous write operations, you must continue to query the task results.
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
        # The SAML assertion consumer URL of the local SP. Configure it in the external IdP.
        self.acs_url = acs_url
        # The entity identifier of the local SP. Configure it in the external IdP. This is not the Entity ID of the external IdP.
        self.entity_id = entity_id
        # The SP metadata XML of the local SP. Use it for import in the external IdP. Do not submit it as the IdP XML for SAML configuration.
        self.metadata_xml = metadata_xml
        # Required. The query parameter. Only the exact value SAML is supported. The response returns SAML.
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

