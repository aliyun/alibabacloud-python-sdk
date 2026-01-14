# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeDataLimitsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeDataLimitsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The data assets.
        self.items = items
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDataLimitsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataLimitsResponseBodyItems(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        auto_scan: int = None,
        check_status: int = None,
        check_status_name: str = None,
        datamask_status: int = None,
        db_version: str = None,
        enable: int = None,
        engine_type: str = None,
        error_code: str = None,
        error_message: str = None,
        event_status: int = None,
        gmt_create: int = None,
        id: int = None,
        instance_description: str = None,
        instance_id: str = None,
        last_finished_time: int = None,
        last_start_time: int = None,
        local_name: str = None,
        log_store_day: int = None,
        member_account: int = None,
        next_start_time: int = None,
        ocr_status: int = None,
        parent_id: str = None,
        port: int = None,
        process_status: int = None,
        process_total_count: int = None,
        region_id: str = None,
        resource_type: int = None,
        resource_type_code: str = None,
        sampling_size: int = None,
        security_group_id_list: List[str] = None,
        support_audit: bool = None,
        support_datamask: bool = None,
        support_event: bool = None,
        support_ocr: bool = None,
        support_scan: bool = None,
        tenant_name: str = None,
        total_count: int = None,
        user_name: str = None,
        v_switch_id_list: List[str] = None,
        vpc_id: str = None,
    ):
        # Indicates whether the security audit feature is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.audit_status = audit_status
        # Indicates whether the data asset can be automatically scanned. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.auto_scan = auto_scan
        # The data detection status. Valid values:
        # 
        # *   **0**: The data detection is ready.
        # *   **1**: The data detection is running.
        # *   **2**: The connectivity test is in progress.
        # *   **3**: The connectivity test is passed.
        # *   **4**: The connectivity test failed.
        self.check_status = check_status
        # The name of the data detection status.
        self.check_status_name = check_status_name
        # Indicates whether DSC has the data de-identification permissions on the data asset. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.datamask_status = datamask_status
        # The database engine version.
        self.db_version = db_version
        # Indicates whether DSC has the data identification permissions on the data asset. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable = enable
        # The type of the database engine. Valid values include **MySQL**, **SQLServer**, **Oracle**, **PostgreSQL**, and **MongoDB**.
        self.engine_type = engine_type
        # The error code.
        self.error_code = error_code
        # The reason for the failure.
        self.error_message = error_message
        # Indicates whether the data leak prevention feature is enabled. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes (default)
        self.event_status = event_status
        # The time when the data asset was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The unique ID of the data asset.
        self.id = id
        # The description of the instance.
        self.instance_description = instance_description
        # The ID of the data asset to which the table belongs.
        self.instance_id = instance_id
        # The time when the last scan is performed.
        # 
        # *   The value is a UNIX timestamp.
        # *   Unit: milliseconds.
        self.last_finished_time = last_finished_time
        # The last scan start time of data assets, in milliseconds.
        self.last_start_time = last_start_time
        # The region in which the data asset resides.
        self.local_name = local_name
        # The retention period of raw logs. Unit: days.
        self.log_store_day = log_store_day
        # The ID of the member.
        self.member_account = member_account
        # The next time when the data asset is scanned. The value is a UNIX timestamp. Unit: milliseconds.
        self.next_start_time = next_start_time
        # Indicates whether the optical character recognition (OCR) feature is enabled. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.ocr_status = ocr_status
        # The parent ID of the data asset that you want to query. Valid values include **bucket, db, and project**.
        self.parent_id = parent_id
        # The port number of the self-managed database.
        self.port = port
        # The status of the data asset scan. Valid values:
        # 
        # *   **-1**: invalid
        # *   **0**: waiting
        # *   **1**: being scanned
        # *   **2**: suspended
        # *   **3**: completed
        self.process_status = process_status
        # The total number of data tables or files.
        self.process_total_count = process_total_count
        # The region in which the asset resides.
        self.region_id = region_id
        # The type of the service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        # *   **6**: self-managed database
        self.resource_type = resource_type
        # The code of the service to which the data asset belongs. Valid values: **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.resource_type_code = resource_type_code
        # The number of sensitive data samples. Valid values: **0**, **5**, and **10**. Unit: data entries.
        self.sampling_size = sampling_size
        # A list of the IDs of the security groups that are used by PrivateLink when you install the DSC agent.
        self.security_group_id_list = security_group_id_list
        # Indicates whether the security audit feature is supported. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.support_audit = support_audit
        # Indicates whether the data de-identification feature is supported. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.support_datamask = support_datamask
        # Indicates whether anomalous event detection is supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.support_event = support_event
        # Indicates whether OCR is supported. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.support_ocr = support_ocr
        # Indicates whether the data asset scan feature is supported. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.support_scan = support_scan
        # The alias of the tenant.
        self.tenant_name = tenant_name
        # The total number of fields in the table.
        self.total_count = total_count
        # The username that is used to access the data asset.
        self.user_name = user_name
        # A list of the IDs of the vSwitches that are used by PrivateLink when you install the DSC agent.
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

        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.check_status_name is not None:
            result['CheckStatusName'] = self.check_status_name

        if self.datamask_status is not None:
            result['DatamaskStatus'] = self.datamask_status

        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_finished_time is not None:
            result['LastFinishedTime'] = self.last_finished_time

        if self.last_start_time is not None:
            result['LastStartTime'] = self.last_start_time

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day

        if self.member_account is not None:
            result['MemberAccount'] = self.member_account

        if self.next_start_time is not None:
            result['NextStartTime'] = self.next_start_time

        if self.ocr_status is not None:
            result['OcrStatus'] = self.ocr_status

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.port is not None:
            result['Port'] = self.port

        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status

        if self.process_total_count is not None:
            result['ProcessTotalCount'] = self.process_total_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_type_code is not None:
            result['ResourceTypeCode'] = self.resource_type_code

        if self.sampling_size is not None:
            result['SamplingSize'] = self.sampling_size

        if self.security_group_id_list is not None:
            result['SecurityGroupIdList'] = self.security_group_id_list

        if self.support_audit is not None:
            result['SupportAudit'] = self.support_audit

        if self.support_datamask is not None:
            result['SupportDatamask'] = self.support_datamask

        if self.support_event is not None:
            result['SupportEvent'] = self.support_event

        if self.support_ocr is not None:
            result['SupportOcr'] = self.support_ocr

        if self.support_scan is not None:
            result['SupportScan'] = self.support_scan

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

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

        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('CheckStatusName') is not None:
            self.check_status_name = m.get('CheckStatusName')

        if m.get('DatamaskStatus') is not None:
            self.datamask_status = m.get('DatamaskStatus')

        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastFinishedTime') is not None:
            self.last_finished_time = m.get('LastFinishedTime')

        if m.get('LastStartTime') is not None:
            self.last_start_time = m.get('LastStartTime')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')

        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')

        if m.get('NextStartTime') is not None:
            self.next_start_time = m.get('NextStartTime')

        if m.get('OcrStatus') is not None:
            self.ocr_status = m.get('OcrStatus')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')

        if m.get('ProcessTotalCount') is not None:
            self.process_total_count = m.get('ProcessTotalCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceTypeCode') is not None:
            self.resource_type_code = m.get('ResourceTypeCode')

        if m.get('SamplingSize') is not None:
            self.sampling_size = m.get('SamplingSize')

        if m.get('SecurityGroupIdList') is not None:
            self.security_group_id_list = m.get('SecurityGroupIdList')

        if m.get('SupportAudit') is not None:
            self.support_audit = m.get('SupportAudit')

        if m.get('SupportDatamask') is not None:
            self.support_datamask = m.get('SupportDatamask')

        if m.get('SupportEvent') is not None:
            self.support_event = m.get('SupportEvent')

        if m.get('SupportOcr') is not None:
            self.support_ocr = m.get('SupportOcr')

        if m.get('SupportScan') is not None:
            self.support_scan = m.get('SupportScan')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VSwitchIdList') is not None:
            self.v_switch_id_list = m.get('VSwitchIdList')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

