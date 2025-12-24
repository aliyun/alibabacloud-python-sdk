# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetLindormV2InstanceSecurityGroupsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        instance_id: str = None,
        request_id: str = None,
        sg_list: List[main_models.GetLindormV2InstanceSecurityGroupsResponseBodySgList] = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.instance_id = instance_id
        self.request_id = request_id
        self.sg_list = sg_list

    def validate(self):
        if self.sg_list:
            for v1 in self.sg_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SgList'] = []
        if self.sg_list is not None:
            for k1 in self.sg_list:
                result['SgList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sg_list = []
        if m.get('SgList') is not None:
            for k1 in m.get('SgList'):
                temp_model = main_models.GetLindormV2InstanceSecurityGroupsResponseBodySgList()
                self.sg_list.append(temp_model.from_map(k1))

        return self

class GetLindormV2InstanceSecurityGroupsResponseBodySgList(DaraModel):
    def __init__(
        self,
        gmt_modified: str = None,
        ip_list: str = None,
        is_available: bool = None,
        security_group_id: str = None,
    ):
        self.gmt_modified = gmt_modified
        self.ip_list = ip_list
        self.is_available = is_available
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

