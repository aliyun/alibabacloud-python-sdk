# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApplicationsRequest(DaraModel):
    def __init__(
        self,
        application_creation_type: str = None,
        application_ids: List[str] = None,
        application_name: str = None,
        authorization_type: str = None,
        instance_id: str = None,
        m_2mclient_status: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_server_status: str = None,
        sso_type: str = None,
        status: str = None,
    ):
        self.application_creation_type = application_creation_type
        # The IDs of the applications.
        self.application_ids = application_ids
        # The name of the application. Only fuzzy match from the leftmost character is supported.
        self.application_name = application_name
        # The authorization of the application. Valid values:
        # 
        # *   authorize_required: Only the user with explicit authorization can access the application.
        # *   default_all: By default, all users can access the application.
        self.authorization_type = authorization_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Used to determine whether M2M client identity is enabled.
        # - enabled
        # - disabled
        self.m_2mclient_status = m_2mclient_status
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # Used to determine whether the ResourceServer capability is enabled.
        # - enabled
        # - disabled
        self.resource_server_status = resource_server_status
        # SSO type.
        # - oidc
        # - saml2
        # - oauth2/m2m
        self.sso_type = sso_type
        # The status of the application. Valid values:
        # 
        # *   Enabled: The application is enabled.
        # *   Disabled: The application is disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_creation_type is not None:
            result['ApplicationCreationType'] = self.application_creation_type

        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.m_2mclient_status is not None:
            result['M2MClientStatus'] = self.m_2mclient_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_server_status is not None:
            result['ResourceServerStatus'] = self.resource_server_status

        if self.sso_type is not None:
            result['SsoType'] = self.sso_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCreationType') is not None:
            self.application_creation_type = m.get('ApplicationCreationType')

        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('M2MClientStatus') is not None:
            self.m_2mclient_status = m.get('M2MClientStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceServerStatus') is not None:
            self.resource_server_status = m.get('ResourceServerStatus')

        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

