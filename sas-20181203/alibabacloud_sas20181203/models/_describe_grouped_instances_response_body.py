# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupedInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeGroupedInstancesResponseBodyInstances] = None,
        page_info: main_models.DescribeGroupedInstancesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about the assets.
        self.instances = instances
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeGroupedInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeGroupedInstancesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGroupedInstancesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGroupedInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        asap_vul_instance_count: int = None,
        auth_version_check_count: int = None,
        field_alias_name: str = None,
        group_flag: int = None,
        instance_core_count: int = None,
        instance_count: str = None,
        os: str = None,
        risk_instance_count: str = None,
        un_protected_instance_count: str = None,
    ):
        # The number of assets on which high-risk vulnerabilities are detected.
        self.asap_vul_instance_count = asap_vul_instance_count
        # The number of assets that are protected by the specified edition.
        self.auth_version_check_count = auth_version_check_count
        # The name of the server group.
        self.field_alias_name = field_alias_name
        # The type of the server group. Valid values:
        # 
        # *   **0**: the default group
        # *   **1**: other group
        self.group_flag = group_flag
        # The number of cores of assets in the specified asset type.
        # 
        # >  If the **MachineTypes** request parameter is not specified, the value of the InstanceCoreCount parameter indicates the total number of cores of assets within your account.
        self.instance_core_count = instance_core_count
        # The total number of assets that belong to the specified type.
        # 
        # >  If the **MachineTypes** request parameter is not specified, the value of the InstanceCount parameter is the total number of your assets.
        self.instance_count = instance_count
        # The operating system type of the asset. Valid values:
        # 
        # * **windows**
        # * **linux**
        # 
        # > This parameter is returned only when Lang is set to zh.
        self.os = os
        # The number of assets that are at risk.
        self.risk_instance_count = risk_instance_count
        # The number of assets that are not protected by Security Center.
        self.un_protected_instance_count = un_protected_instance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asap_vul_instance_count is not None:
            result['AsapVulInstanceCount'] = self.asap_vul_instance_count

        if self.auth_version_check_count is not None:
            result['AuthVersionCheckCount'] = self.auth_version_check_count

        if self.field_alias_name is not None:
            result['FieldAliasName'] = self.field_alias_name

        if self.group_flag is not None:
            result['GroupFlag'] = self.group_flag

        if self.instance_core_count is not None:
            result['InstanceCoreCount'] = self.instance_core_count

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.os is not None:
            result['Os'] = self.os

        if self.risk_instance_count is not None:
            result['RiskInstanceCount'] = self.risk_instance_count

        if self.un_protected_instance_count is not None:
            result['UnProtectedInstanceCount'] = self.un_protected_instance_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsapVulInstanceCount') is not None:
            self.asap_vul_instance_count = m.get('AsapVulInstanceCount')

        if m.get('AuthVersionCheckCount') is not None:
            self.auth_version_check_count = m.get('AuthVersionCheckCount')

        if m.get('FieldAliasName') is not None:
            self.field_alias_name = m.get('FieldAliasName')

        if m.get('GroupFlag') is not None:
            self.group_flag = m.get('GroupFlag')

        if m.get('InstanceCoreCount') is not None:
            self.instance_core_count = m.get('InstanceCoreCount')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('RiskInstanceCount') is not None:
            self.risk_instance_count = m.get('RiskInstanceCount')

        if m.get('UnProtectedInstanceCount') is not None:
            self.un_protected_instance_count = m.get('UnProtectedInstanceCount')

        return self

