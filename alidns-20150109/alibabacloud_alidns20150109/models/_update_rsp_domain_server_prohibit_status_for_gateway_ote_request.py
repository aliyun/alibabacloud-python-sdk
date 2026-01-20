# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateRspDomainServerProhibitStatusForGatewayOteRequest(DaraModel):
    def __init__(
        self,
        add_status_list: List[main_models.UpdateRspDomainServerProhibitStatusForGatewayOteRequestAddStatusList] = None,
        client_token: str = None,
        delete_status_list: List[main_models.UpdateRspDomainServerProhibitStatusForGatewayOteRequestDeleteStatusList] = None,
        domain_name: str = None,
    ):
        self.add_status_list = add_status_list
        # This parameter is required.
        self.client_token = client_token
        self.delete_status_list = delete_status_list
        # This parameter is required.
        self.domain_name = domain_name

    def validate(self):
        if self.add_status_list:
            for v1 in self.add_status_list:
                 if v1:
                    v1.validate()
        if self.delete_status_list:
            for v1 in self.delete_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddStatusList'] = []
        if self.add_status_list is not None:
            for k1 in self.add_status_list:
                result['AddStatusList'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['DeleteStatusList'] = []
        if self.delete_status_list is not None:
            for k1 in self.delete_status_list:
                result['DeleteStatusList'].append(k1.to_map() if k1 else None)

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_status_list = []
        if m.get('AddStatusList') is not None:
            for k1 in m.get('AddStatusList'):
                temp_model = main_models.UpdateRspDomainServerProhibitStatusForGatewayOteRequestAddStatusList()
                self.add_status_list.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.delete_status_list = []
        if m.get('DeleteStatusList') is not None:
            for k1 in m.get('DeleteStatusList'):
                temp_model = main_models.UpdateRspDomainServerProhibitStatusForGatewayOteRequestDeleteStatusList()
                self.delete_status_list.append(temp_model.from_map(k1))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

class UpdateRspDomainServerProhibitStatusForGatewayOteRequestDeleteStatusList(DaraModel):
    def __init__(
        self,
        status: str = None,
        status_msg: str = None,
    ):
        self.status = status
        self.status_msg = status_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.status_msg is not None:
            result['StatusMsg'] = self.status_msg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMsg') is not None:
            self.status_msg = m.get('StatusMsg')

        return self

class UpdateRspDomainServerProhibitStatusForGatewayOteRequestAddStatusList(DaraModel):
    def __init__(
        self,
        status: str = None,
        status_msg: str = None,
    ):
        self.status = status
        self.status_msg = status_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.status_msg is not None:
            result['StatusMsg'] = self.status_msg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMsg') is not None:
            self.status_msg = m.get('StatusMsg')

        return self

