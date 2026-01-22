# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeGdnInstancesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeGdnInstancesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeGdnInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeGdnInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        gdn_instance_list: List[main_models.DescribeGdnInstancesResponseBodyDataGdnInstanceList] = None,
        page_number: str = None,
        page_size: str = None,
        total_number: str = None,
    ):
        self.gdn_instance_list = gdn_instance_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_number = total_number

    def validate(self):
        if self.gdn_instance_list:
            for v1 in self.gdn_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GdnInstanceList'] = []
        if self.gdn_instance_list is not None:
            for k1 in self.gdn_instance_list:
                result['GdnInstanceList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_number is not None:
            result['TotalNumber'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gdn_instance_list = []
        if m.get('GdnInstanceList') is not None:
            for k1 in m.get('GdnInstanceList'):
                temp_model = main_models.DescribeGdnInstancesResponseBodyDataGdnInstanceList()
                self.gdn_instance_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')

        return self

class DescribeGdnInstancesResponseBodyDataGdnInstanceList(DaraModel):
    def __init__(
        self,
        description: str = None,
        gdn_instance_name: str = None,
        gdn_mode: str = None,
        gmt_created: str = None,
        member_list: List[main_models.DescribeGdnInstancesResponseBodyDataGdnInstanceListMemberList] = None,
        mysql_version: str = None,
        rpl_conflict_strategy: str = None,
        rpl_dml_strategy: str = None,
        rpl_sync_ddl: bool = None,
        status: str = None,
        switch_history: str = None,
    ):
        self.description = description
        self.gdn_instance_name = gdn_instance_name
        self.gdn_mode = gdn_mode
        self.gmt_created = gmt_created
        self.member_list = member_list
        self.mysql_version = mysql_version
        self.rpl_conflict_strategy = rpl_conflict_strategy
        self.rpl_dml_strategy = rpl_dml_strategy
        self.rpl_sync_ddl = rpl_sync_ddl
        self.status = status
        self.switch_history = switch_history

    def validate(self):
        if self.member_list:
            for v1 in self.member_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gdn_instance_name is not None:
            result['GdnInstanceName'] = self.gdn_instance_name

        if self.gdn_mode is not None:
            result['GdnMode'] = self.gdn_mode

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        result['MemberList'] = []
        if self.member_list is not None:
            for k1 in self.member_list:
                result['MemberList'].append(k1.to_map() if k1 else None)

        if self.mysql_version is not None:
            result['MysqlVersion'] = self.mysql_version

        if self.rpl_conflict_strategy is not None:
            result['RplConflictStrategy'] = self.rpl_conflict_strategy

        if self.rpl_dml_strategy is not None:
            result['RplDmlStrategy'] = self.rpl_dml_strategy

        if self.rpl_sync_ddl is not None:
            result['RplSyncDdl'] = self.rpl_sync_ddl

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_history is not None:
            result['SwitchHistory'] = self.switch_history

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GdnInstanceName') is not None:
            self.gdn_instance_name = m.get('GdnInstanceName')

        if m.get('GdnMode') is not None:
            self.gdn_mode = m.get('GdnMode')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        self.member_list = []
        if m.get('MemberList') is not None:
            for k1 in m.get('MemberList'):
                temp_model = main_models.DescribeGdnInstancesResponseBodyDataGdnInstanceListMemberList()
                self.member_list.append(temp_model.from_map(k1))

        if m.get('MysqlVersion') is not None:
            self.mysql_version = m.get('MysqlVersion')

        if m.get('RplConflictStrategy') is not None:
            self.rpl_conflict_strategy = m.get('RplConflictStrategy')

        if m.get('RplDmlStrategy') is not None:
            self.rpl_dml_strategy = m.get('RplDmlStrategy')

        if m.get('RplSyncDdl') is not None:
            self.rpl_sync_ddl = m.get('RplSyncDdl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchHistory') is not None:
            self.switch_history = m.get('SwitchHistory')

        return self

class DescribeGdnInstancesResponseBodyDataGdnInstanceListMemberList(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        cn_node_class_code: str = None,
        cn_node_count: str = None,
        commodity_code: str = None,
        data_sync_status: str = None,
        dn_node_class_code: str = None,
        dn_node_count: str = None,
        expire_time: str = None,
        gmt_created: str = None,
        member_name: str = None,
        pay_type: str = None,
        primary_zone: str = None,
        read_write_status: str = None,
        region_id: str = None,
        role: str = None,
        secondary_zone: str = None,
        seconds_behind_master: str = None,
        status: str = None,
        task_status: str = None,
        tertiary_zone: str = None,
        zone_id: str = None,
    ):
        self.class_code = class_code
        self.cn_node_class_code = cn_node_class_code
        self.cn_node_count = cn_node_count
        self.commodity_code = commodity_code
        self.data_sync_status = data_sync_status
        self.dn_node_class_code = dn_node_class_code
        self.dn_node_count = dn_node_count
        self.expire_time = expire_time
        self.gmt_created = gmt_created
        self.member_name = member_name
        self.pay_type = pay_type
        self.primary_zone = primary_zone
        self.read_write_status = read_write_status
        self.region_id = region_id
        self.role = role
        self.secondary_zone = secondary_zone
        self.seconds_behind_master = seconds_behind_master
        self.status = status
        self.task_status = task_status
        self.tertiary_zone = tertiary_zone
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.cn_node_class_code is not None:
            result['CnNodeClassCode'] = self.cn_node_class_code

        if self.cn_node_count is not None:
            result['CnNodeCount'] = self.cn_node_count

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.data_sync_status is not None:
            result['DataSyncStatus'] = self.data_sync_status

        if self.dn_node_class_code is not None:
            result['DnNodeClassCode'] = self.dn_node_class_code

        if self.dn_node_count is not None:
            result['DnNodeCount'] = self.dn_node_count

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone

        if self.read_write_status is not None:
            result['ReadWriteStatus'] = self.read_write_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role is not None:
            result['Role'] = self.role

        if self.secondary_zone is not None:
            result['SecondaryZone'] = self.secondary_zone

        if self.seconds_behind_master is not None:
            result['SecondsBehindMaster'] = self.seconds_behind_master

        if self.status is not None:
            result['Status'] = self.status

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.tertiary_zone is not None:
            result['TertiaryZone'] = self.tertiary_zone

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('CnNodeClassCode') is not None:
            self.cn_node_class_code = m.get('CnNodeClassCode')

        if m.get('CnNodeCount') is not None:
            self.cn_node_count = m.get('CnNodeCount')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('DataSyncStatus') is not None:
            self.data_sync_status = m.get('DataSyncStatus')

        if m.get('DnNodeClassCode') is not None:
            self.dn_node_class_code = m.get('DnNodeClassCode')

        if m.get('DnNodeCount') is not None:
            self.dn_node_count = m.get('DnNodeCount')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')

        if m.get('ReadWriteStatus') is not None:
            self.read_write_status = m.get('ReadWriteStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SecondaryZone') is not None:
            self.secondary_zone = m.get('SecondaryZone')

        if m.get('SecondsBehindMaster') is not None:
            self.seconds_behind_master = m.get('SecondsBehindMaster')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TertiaryZone') is not None:
            self.tertiary_zone = m.get('TertiaryZone')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

