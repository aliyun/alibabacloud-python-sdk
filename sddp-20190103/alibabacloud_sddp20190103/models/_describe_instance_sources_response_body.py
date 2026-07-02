# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceSourcesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeInstanceSourcesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # A list of assets.
        self.items = items
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of assets.
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
                temp_model = main_models.DescribeInstanceSourcesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceSourcesResponseBodyItems(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        auto_scan: int = None,
        can_modify_user_name: bool = None,
        check_status: int = None,
        datamask_status: int = None,
        db_name: str = None,
        enable: int = None,
        engine_type: str = None,
        error_message: str = None,
        gmt_create: int = None,
        id: int = None,
        instance_description: str = None,
        instance_id: str = None,
        instance_size: int = None,
        last_modify_time: int = None,
        last_modify_user_id: str = None,
        log_store_day: int = None,
        password_status: int = None,
        product_id: int = None,
        region_id: str = None,
        region_name: str = None,
        sampling_size: int = None,
        tenant_id: str = None,
        tenant_name: str = None,
        user_name: str = None,
    ):
        # The audit authorization status. Valid values:
        # 
        # - **1**: Authorized.
        # 
        # - **0**: Unauthorized.
        self.audit_status = audit_status
        # Indicates whether automatic scanning for sensitive data is enabled. Valid values:
        # 
        # - **0**: Disabled.
        # 
        # - **1**: Enabled.
        self.auto_scan = auto_scan
        # Indicates whether the username and password can be modified. Valid values:
        # 
        # - **true**: Yes.
        # 
        # - **false**: No.
        self.can_modify_user_name = can_modify_user_name
        # The data check status. Valid values:
        # 
        # - **0**: Ready.
        # 
        # - **1**: Running.
        # 
        # - **2**: Connectivity test in progress.
        # 
        # - **3**: Connectivity test passed.
        # 
        # - **4**: Connectivity test failed.
        self.check_status = check_status
        # The status of data masking authorization. Valid values:
        # 
        # - **1**: Enabled.
        # 
        # - **0**: Disabled.
        self.datamask_status = datamask_status
        # The name of the database to which the asset belongs.
        self.db_name = db_name
        # Indicates whether sensitive data detection is enabled for the asset. Valid values:
        # 
        # - **1**: Enabled.
        # 
        # - **0**: Disabled.
        self.enable = enable
        # The database engine type. Valid values:
        # 
        # - **MySQL**
        # 
        # - **MariaDB**
        # 
        # - **Oracle**
        # 
        # - **PostgreSQL**
        # 
        # - **SQLServer**
        self.engine_type = engine_type
        # The reason for the failure.
        self.error_message = error_message
        # The time when the asset was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The unique ID of the asset.
        self.id = id
        # The description of the instance.
        self.instance_description = instance_description
        # The instance ID.
        self.instance_id = instance_id
        # The size of the instance. This parameter is valid only for OSS assets. Unit: bytes.
        self.instance_size = instance_size
        # The timestamp when the asset was last modified. Unit: milliseconds.
        self.last_modify_time = last_modify_time
        # The ID of the account that last modified the asset.
        self.last_modify_user_id = last_modify_user_id
        # The storage duration of raw logs. Unit: days.
        self.log_store_day = log_store_day
        # The status of the password. Valid values:
        # 
        # - **1**: In use.
        # 
        # - **0**: Not in use.
        self.password_status = password_status
        # The product type ID. Valid values:
        # 
        # - **1**: MaxCompute
        # 
        # - **2**: OSS
        # 
        # - **3**: ADS
        # 
        # - **4**: OTS
        # 
        # - **5**: RDS
        # 
        # - **6**: SELF_DB
        self.product_id = product_id
        # The region ID.
        self.region_id = region_id
        # The name of the region.
        self.region_name = region_name
        # The sensitive data sampling size. Valid values: **0**, **5**, and **10**. Unit: number of entries.
        self.sampling_size = sampling_size
        # The tenant ID.
        self.tenant_id = tenant_id
        # The name of the tenant.
        self.tenant_name = tenant_name
        # The username of the account.
        self.user_name = user_name

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

        if self.can_modify_user_name is not None:
            result['CanModifyUserName'] = self.can_modify_user_name

        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.datamask_status is not None:
            result['DatamaskStatus'] = self.datamask_status

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_size is not None:
            result['InstanceSize'] = self.instance_size

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.last_modify_user_id is not None:
            result['LastModifyUserId'] = self.last_modify_user_id

        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day

        if self.password_status is not None:
            result['PasswordStatus'] = self.password_status

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.sampling_size is not None:
            result['SamplingSize'] = self.sampling_size

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')

        if m.get('CanModifyUserName') is not None:
            self.can_modify_user_name = m.get('CanModifyUserName')

        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('DatamaskStatus') is not None:
            self.datamask_status = m.get('DatamaskStatus')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSize') is not None:
            self.instance_size = m.get('InstanceSize')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('LastModifyUserId') is not None:
            self.last_modify_user_id = m.get('LastModifyUserId')

        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')

        if m.get('PasswordStatus') is not None:
            self.password_status = m.get('PasswordStatus')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('SamplingSize') is not None:
            self.sampling_size = m.get('SamplingSize')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

