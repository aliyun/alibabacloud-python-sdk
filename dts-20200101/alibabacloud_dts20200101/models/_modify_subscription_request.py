# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySubscriptionRequest(DaraModel):
    def __init__(
        self,
        db_list: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        modify_type: str = None,
        region_id: str = None,
        reserved: str = None,
        resource_group_id: str = None,
        subscription_data_type_ddl: bool = None,
        subscription_data_type_dml: bool = None,
    ):
        # The objects of the change tracking task. The value is a JSON string. For more information, see [Objects of DTS tasks](https://help.aliyun.com/document_detail/209545.html).
        # 
        # >  You can call the [DescribeDtsJobDetail](https://help.aliyun.com/document_detail/208925.html) operation to query the original objects of the task.
        self.db_list = db_list
        # The ID of the change tracking instance. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the instance ID.
        self.dts_instance_id = dts_instance_id
        # The ID of the change tracking task. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        self.dts_job_id = dts_job_id
        self.modify_type = modify_type
        # The ID of the region where the change tracking instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        self.reserved = reserved
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to retrieve data definition language (DDL) statements. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.subscription_data_type_ddl = subscription_data_type_ddl
        # Specifies whether to retrieve data manipulation language (DML) statements. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.subscription_data_type_dml = subscription_data_type_dml

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_list is not None:
            result['DbList'] = self.db_list

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.subscription_data_type_ddl is not None:
            result['SubscriptionDataTypeDDL'] = self.subscription_data_type_ddl

        if self.subscription_data_type_dml is not None:
            result['SubscriptionDataTypeDML'] = self.subscription_data_type_dml

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SubscriptionDataTypeDDL') is not None:
            self.subscription_data_type_ddl = m.get('SubscriptionDataTypeDDL')

        if m.get('SubscriptionDataTypeDML') is not None:
            self.subscription_data_type_dml = m.get('SubscriptionDataTypeDML')

        return self

