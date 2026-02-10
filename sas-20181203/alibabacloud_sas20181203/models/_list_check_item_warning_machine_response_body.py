# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCheckItemWarningMachineResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListCheckItemWarningMachineResponseBodyList] = None,
        page_info: main_models.ListCheckItemWarningMachineResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The servers on which the alerts are generated.
        self.list = list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListCheckItemWarningMachineResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListCheckItemWarningMachineResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCheckItemWarningMachineResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of affected assets returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of affected assets.
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

class ListCheckItemWarningMachineResponseBodyList(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        auth_version: int = None,
        bind: bool = None,
        container_id: str = None,
        container_name: str = None,
        fix_list: List[main_models.ListCheckItemWarningMachineResponseBodyListFixList] = None,
        fix_status: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        last_handle_time: int = None,
        last_scan_time: int = None,
        port_open: bool = None,
        prompt: str = None,
        region_id: str = None,
        status: int = None,
        target_id: str = None,
        target_name: str = None,
        target_type: str = None,
        uuid: str = None,
        warning_risk_list: List[main_models.ListCheckItemWarningMachineResponseBodyListWarningRiskList] = None,
    ):
        # 云产品资产的类型。
        self.asset_type = asset_type
        # The edition of Security Center that is authorized to protect the asset. Valid values:
        # 
        # *   **1**: Basic edition
        # *   **6**: Anti-virus edition
        # *   **5**: Advanced edition
        # *   **3**: Enterprise edition
        # *   **7**: Ultimate edition
        # *   **10**: Value-added Plan edition
        self.auth_version = auth_version
        # Indicates whether Security Center is authorized to protect the asset. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.bind = bind
        # The ID of the container.
        self.container_id = container_id
        # The name of the container.
        self.container_name = container_name
        # The details of the baselines for which the risk item can be fixed.
        self.fix_list = fix_list
        # Whether the repair is supported. Valid values:
        # *   **0**: Supported
        # *   **1**: Not Supported
        self.fix_status = fix_status
        # The instance ID of the server.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The public IP address of the affected asset.
        self.internet_ip = internet_ip
        # The private IP address of the affected asset.
        self.intranet_ip = intranet_ip
        # The timestamp of the latest processing of the check item risk of the machine. Unit: milliseconds.
        self.last_handle_time = last_handle_time
        # The timestamp generated when the last scan was performed. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # Indicates whether a port on the server is accessible over the Internet. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.port_open = port_open
        # The prompt for the risk item.
        self.prompt = prompt
        # The region ID of the asset.
        self.region_id = region_id
        # The status of the check item. Valid values:
        # 
        # *   **1**: failed
        # *   **2**: verifying
        # *   **3**: passed
        # *   **6**: ignored
        # *   **7**: fixing
        # *   **8**: fixed
        self.status = status
        # The ID of the asset that is scanned.
        self.target_id = target_id
        # The name of the asset on which the malicious image sample is detected.
        self.target_name = target_name
        # The type of the asset. Valid values:
        # 
        # *   **ECS_SNAPSHOT**
        # *   **ECS_IMAGE**
        self.target_type = target_type
        # The UUID of the server.
        self.uuid = uuid
        # The information about the baselines on which the risk item is detected.
        self.warning_risk_list = warning_risk_list

    def validate(self):
        if self.fix_list:
            for v1 in self.fix_list:
                 if v1:
                    v1.validate()
        if self.warning_risk_list:
            for v1 in self.warning_risk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.auth_version is not None:
            result['AuthVersion'] = self.auth_version

        if self.bind is not None:
            result['Bind'] = self.bind

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        result['FixList'] = []
        if self.fix_list is not None:
            for k1 in self.fix_list:
                result['FixList'].append(k1.to_map() if k1 else None)

        if self.fix_status is not None:
            result['FixStatus'] = self.fix_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.last_handle_time is not None:
            result['LastHandleTime'] = self.last_handle_time

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.port_open is not None:
            result['PortOpen'] = self.port_open

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        result['WarningRiskList'] = []
        if self.warning_risk_list is not None:
            for k1 in self.warning_risk_list:
                result['WarningRiskList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AuthVersion') is not None:
            self.auth_version = m.get('AuthVersion')

        if m.get('Bind') is not None:
            self.bind = m.get('Bind')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        self.fix_list = []
        if m.get('FixList') is not None:
            for k1 in m.get('FixList'):
                temp_model = main_models.ListCheckItemWarningMachineResponseBodyListFixList()
                self.fix_list.append(temp_model.from_map(k1))

        if m.get('FixStatus') is not None:
            self.fix_status = m.get('FixStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LastHandleTime') is not None:
            self.last_handle_time = m.get('LastHandleTime')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('PortOpen') is not None:
            self.port_open = m.get('PortOpen')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        self.warning_risk_list = []
        if m.get('WarningRiskList') is not None:
            for k1 in m.get('WarningRiskList'):
                temp_model = main_models.ListCheckItemWarningMachineResponseBodyListWarningRiskList()
                self.warning_risk_list.append(temp_model.from_map(k1))

        return self

class ListCheckItemWarningMachineResponseBodyListWarningRiskList(DaraModel):
    def __init__(
        self,
        risk_id: int = None,
        risk_name: str = None,
    ):
        # The ID of the baseline.
        self.risk_id = risk_id
        # The name of the baseline.
        self.risk_name = risk_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        return self

class ListCheckItemWarningMachineResponseBodyListFixList(DaraModel):
    def __init__(
        self,
        risk_id: int = None,
        risk_name: str = None,
    ):
        # The ID of the baseline.
        self.risk_id = risk_id
        # The name of the baseline.
        self.risk_name = risk_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        return self

