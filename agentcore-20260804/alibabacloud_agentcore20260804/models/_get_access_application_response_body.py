# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetAccessApplicationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAccessApplicationResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The access application details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request processing result message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.GetAccessApplicationResponseBodyData()
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

class GetAccessApplicationResponseBodyData(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        client_id: str = None,
        created_at: str = None,
        metadata_url: str = None,
        redirect_uris: List[str] = None,
        updated_at: str = None,
        user_source: str = None,
        workspace_id: str = None,
    ):
        # The access application ID.
        self.application_id = application_id
        # The name of the access application.
        self.application_name = application_name
        # The OAuth client ID.
        self.client_id = client_id
        # The creation time in RFC 3339 format.
        self.created_at = created_at
        # The metadata URL of the identity provider.
        self.metadata_url = metadata_url
        # The list of redirect URIs.
        self.redirect_uris = redirect_uris
        # The update time in RFC 3339 format.
        self.updated_at = updated_at
        # The user source.
        self.user_source = user_source
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['applicationId'] = self.application_id

        if self.application_name is not None:
            result['applicationName'] = self.application_name

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.metadata_url is not None:
            result['metadataUrl'] = self.metadata_url

        if self.redirect_uris is not None:
            result['redirectUris'] = self.redirect_uris

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.user_source is not None:
            result['userSource'] = self.user_source

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationId') is not None:
            self.application_id = m.get('applicationId')

        if m.get('applicationName') is not None:
            self.application_name = m.get('applicationName')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('metadataUrl') is not None:
            self.metadata_url = m.get('metadataUrl')

        if m.get('redirectUris') is not None:
            self.redirect_uris = m.get('redirectUris')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('userSource') is not None:
            self.user_source = m.get('userSource')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

