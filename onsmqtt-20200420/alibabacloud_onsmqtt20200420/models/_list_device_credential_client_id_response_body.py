# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class ListDeviceCredentialClientIdResponseBody(DaraModel):
    def __init__(
        self,
        device_credential_client_id_list: main_models.ListDeviceCredentialClientIdResponseBodyDeviceCredentialClientIdList = None,
        request_id: str = None,
    ):
        # Returns the information list.
        self.device_credential_client_id_list = device_credential_client_id_list
        # Public parameters, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id

    def validate(self):
        if self.device_credential_client_id_list:
            self.device_credential_client_id_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_credential_client_id_list is not None:
            result['DeviceCredentialClientIdList'] = self.device_credential_client_id_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCredentialClientIdList') is not None:
            temp_model = main_models.ListDeviceCredentialClientIdResponseBodyDeviceCredentialClientIdList()
            self.device_credential_client_id_list = temp_model.from_map(m.get('DeviceCredentialClientIdList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDeviceCredentialClientIdResponseBodyDeviceCredentialClientIdList(DaraModel):
    def __init__(
        self,
        client_id_list: List[str] = None,
        next_token: str = None,
        page_no: str = None,
        page_size: str = None,
        total: str = None,
    ):
        # Client list.
        self.client_id_list = client_id_list
        # Indicates whether there is a token (Token) for the next query. Values:
        # 
        # - For the first query and when there is no next query, this field does not need to be filled.
        # 
        # - If there is a next query, the value should be the NextToken returned from the previous API call.
        self.next_token = next_token
        # The current page number of the returned query records.
        self.page_no = page_no
        # The maximum number of results to display per page.
        self.page_size = page_size
        # Total number of query results.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id_list is not None:
            result['ClientIdList'] = self.client_id_list

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIdList') is not None:
            self.client_id_list = m.get('ClientIdList')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

