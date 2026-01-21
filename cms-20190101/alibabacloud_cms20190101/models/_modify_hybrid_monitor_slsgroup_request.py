# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class ModifyHybridMonitorSLSGroupRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        slsgroup_config: List[main_models.ModifyHybridMonitorSLSGroupRequestSLSGroupConfig] = None,
        slsgroup_description: str = None,
        slsgroup_name: str = None,
    ):
        self.region_id = region_id
        # The configurations of the Logstore group.
        # 
        # Valid values of N: 1 to 25.
        # 
        # This parameter is required.
        self.slsgroup_config = slsgroup_config
        # The description of the Logstore group.
        self.slsgroup_description = slsgroup_description
        # The name of the Logstore group.
        # 
        # For information about how to obtain the name of a Logstore group, see [DescribeHybridMonitorSLSGroup](https://help.aliyun.com/document_detail/429526.html).
        # 
        # This parameter is required.
        self.slsgroup_name = slsgroup_name

    def validate(self):
        if self.slsgroup_config:
            for v1 in self.slsgroup_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['SLSGroupConfig'] = []
        if self.slsgroup_config is not None:
            for k1 in self.slsgroup_config:
                result['SLSGroupConfig'].append(k1.to_map() if k1 else None)

        if self.slsgroup_description is not None:
            result['SLSGroupDescription'] = self.slsgroup_description

        if self.slsgroup_name is not None:
            result['SLSGroupName'] = self.slsgroup_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.slsgroup_config = []
        if m.get('SLSGroupConfig') is not None:
            for k1 in m.get('SLSGroupConfig'):
                temp_model = main_models.ModifyHybridMonitorSLSGroupRequestSLSGroupConfig()
                self.slsgroup_config.append(temp_model.from_map(k1))

        if m.get('SLSGroupDescription') is not None:
            self.slsgroup_description = m.get('SLSGroupDescription')

        if m.get('SLSGroupName') is not None:
            self.slsgroup_name = m.get('SLSGroupName')

        return self

class ModifyHybridMonitorSLSGroupRequestSLSGroupConfig(DaraModel):
    def __init__(
        self,
        slslogstore: str = None,
        slsproject: str = None,
        slsregion: str = None,
        slsuser_id: str = None,
    ):
        # The Logstore.
        # 
        # Valid values of N: 1 to 25.
        # 
        # This parameter is required.
        self.slslogstore = slslogstore
        # The Simple Log Service project.
        # 
        # Valid values of N: 1 to 25.
        # 
        # This parameter is required.
        self.slsproject = slsproject
        # The region ID.
        # 
        # Valid values of N: 1 to 25.
        # 
        # This parameter is required.
        self.slsregion = slsregion
        # The member ID.
        # 
        # Valid values of N: 1 to 25.
        # 
        # If you call this operation by using the management account of a resource directory, you can connect the Alibaba Cloud services that are activated for all members in the resource directory to Hybrid Cloud Monitoring. You can use the resource directory to monitor Alibaba Cloud services across enterprise accounts.
        # 
        # > If a member uses CloudMonitor for the first time, you must make sure that the service-linked role AliyunServiceRoleForCloudMonitor is attached to the member. For more information, see [Manage the service-linked role for CloudMonitor](https://help.aliyun.com/document_detail/170423.html).
        self.slsuser_id = slsuser_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.slslogstore is not None:
            result['SLSLogstore'] = self.slslogstore

        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject

        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion

        if self.slsuser_id is not None:
            result['SLSUserId'] = self.slsuser_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SLSLogstore') is not None:
            self.slslogstore = m.get('SLSLogstore')

        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')

        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')

        if m.get('SLSUserId') is not None:
            self.slsuser_id = m.get('SLSUserId')

        return self

