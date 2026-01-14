# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyDataLimitRequest(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        auto_scan: int = None,
        engine_type: str = None,
        feature_type: int = None,
        id: int = None,
        lang: str = None,
        log_store_day: int = None,
        modify_password: bool = None,
        password: str = None,
        port: int = None,
        resource_type: int = None,
        sampling_size: int = None,
        security_group_id_list: List[str] = None,
        service_region_id: str = None,
        user_name: str = None,
        v_switch_id_list: List[str] = None,
        vpc_id: str = None,
    ):
        # Specifies whether to enable the security audit feature. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.audit_status = audit_status
        # Specifies whether to automatically trigger a re-scan after a rule is modified. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # > When a re-scan is triggered, DSC scans all data in your data asset.
        self.auto_scan = auto_scan
        # The database engine that is run by the instance. Valid values:
        # 
        # *   **MySQL**
        # *   **SQLServer**
        self.engine_type = engine_type
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The unique ID of the data asset for which you want to modify configuration items.
        # 
        # > You can call the [DescribeDataLimits](~~DescribeDataLimits~~) operation to query the ID of the data asset.
        # 
        # This parameter is required.
        self.id = id
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The retention period of raw logs after you enable the security audit feature. Unit: days. Valid values:
        # 
        # *   **30**
        # *   **90**
        # *   **180**
        # *   **365**
        self.log_store_day = log_store_day
        # Specifies whether to change the username and password that are used to log on to the ApsaraDB RDS database. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.modify_password = modify_password
        # The password used to log on to the ApsaraDB RDS database that you authorize DSC to access.
        self.password = password
        # The port that is used to connect to the database.
        self.port = port
        # The name of the service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: Object Storage Service (OSS)
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The number of sensitive data samples tht are collected after sensitive data detection is enabled. Valid values:
        # 
        # *   **0**
        # *   **5**
        # *   **10**
        self.sampling_size = sampling_size
        # The security group that is used by PrivateLink when you install the DSC agent.
        self.security_group_id_list = security_group_id_list
        # The region in which the data asset resides. Valid values:
        # 
        # *   **cn-beijing**: China (Beijing)
        # *   **cn-zhangjiakou**: China (Zhangjiakou)
        # *   **cn-huhehaote**: China (Hohhot)
        # *   **cn-hangzhou**: China (Hangzhou)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-hongkong**: China (Hong Kong)
        self.service_region_id = service_region_id
        # The username used to log on to the ApsaraDB RDS database that you authorize DSC to access.
        self.user_name = user_name
        # The vSwitch that is used by PrivateLink when you install the DSC agent.
        self.v_switch_id_list = v_switch_id_list
        # The ID of the virtual private cloud (VPC) to which the data asset belongs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.auto_scan is not None:
            result['AutoScan'] = self.auto_scan

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day

        if self.modify_password is not None:
            result['ModifyPassword'] = self.modify_password

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sampling_size is not None:
            result['SamplingSize'] = self.sampling_size

        if self.security_group_id_list is not None:
            result['SecurityGroupIdList'] = self.security_group_id_list

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.v_switch_id_list is not None:
            result['VSwitchIdList'] = self.v_switch_id_list

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')

        if m.get('ModifyPassword') is not None:
            self.modify_password = m.get('ModifyPassword')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SamplingSize') is not None:
            self.sampling_size = m.get('SamplingSize')

        if m.get('SecurityGroupIdList') is not None:
            self.security_group_id_list = m.get('SecurityGroupIdList')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VSwitchIdList') is not None:
            self.v_switch_id_list = m.get('VSwitchIdList')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

