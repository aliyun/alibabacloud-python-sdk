# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeAuditLogsResponseBody(DaraModel):
    def __init__(
        self,
        async_request_id: str = None,
        current_page: int = None,
        items: List[main_models.DescribeAuditLogsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.async_request_id = async_request_id
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
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
        if self.async_request_id is not None:
            result['AsyncRequestId'] = self.async_request_id

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
        if m.get('AsyncRequestId') is not None:
            self.async_request_id = m.get('AsyncRequestId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAuditLogsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self



class DescribeAuditLogsResponseBodyItems(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        client_port: str = None,
        client_ua: str = None,
        column_name: str = None,
        creation_time: int = None,
        data_set: str = None,
        database_name: str = None,
        db_type: str = None,
        effect_row: int = None,
        execute_status: int = None,
        execute_time: int = None,
        in_white_list: bool = None,
        instance_audit_status: str = None,
        instance_description: str = None,
        instance_name: str = None,
        ip_type: str = None,
        log_source: str = None,
        log_time: int = None,
        member_account: str = None,
        message: str = None,
        model_name: str = None,
        operate_type: str = None,
        oss_object_key: str = None,
        package_name: str = None,
        product_code: str = None,
        product_id: int = None,
        rule_category: str = None,
        rule_id: str = None,
        rule_name: str = None,
        sql_text: str = None,
        table_name: str = None,
        user_id: str = None,
        user_name: str = None,
        warn_level: str = None,
        warn_level_name: str = None,
    ):
        self.client_ip = client_ip
        self.client_port = client_port
        self.client_ua = client_ua
        self.column_name = column_name
        self.creation_time = creation_time
        self.data_set = data_set
        self.database_name = database_name
        self.db_type = db_type
        self.effect_row = effect_row
        self.execute_status = execute_status
        self.execute_time = execute_time
        self.in_white_list = in_white_list
        self.instance_audit_status = instance_audit_status
        self.instance_description = instance_description
        self.instance_name = instance_name
        self.ip_type = ip_type
        self.log_source = log_source
        self.log_time = log_time
        self.member_account = member_account
        self.message = message
        self.model_name = model_name
        self.operate_type = operate_type
        self.oss_object_key = oss_object_key
        self.package_name = package_name
        self.product_code = product_code
        self.product_id = product_id
        self.rule_category = rule_category
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.sql_text = sql_text
        self.table_name = table_name
        self.user_id = user_id
        self.user_name = user_name
        self.warn_level = warn_level
        self.warn_level_name = warn_level_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_port is not None:
            result['ClientPort'] = self.client_port

        if self.client_ua is not None:
            result['ClientUa'] = self.client_ua

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_set is not None:
            result['DataSet'] = self.data_set

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.effect_row is not None:
            result['EffectRow'] = self.effect_row

        if self.execute_status is not None:
            result['ExecuteStatus'] = self.execute_status

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.in_white_list is not None:
            result['InWhiteList'] = self.in_white_list

        if self.instance_audit_status is not None:
            result['InstanceAuditStatus'] = self.instance_audit_status

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.log_source is not None:
            result['LogSource'] = self.log_source

        if self.log_time is not None:
            result['LogTime'] = self.log_time

        if self.member_account is not None:
            result['MemberAccount'] = self.member_account

        if self.message is not None:
            result['Message'] = self.message

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.oss_object_key is not None:
            result['OssObjectKey'] = self.oss_object_key

        if self.package_name is not None:
            result['PackageName'] = self.package_name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.rule_category is not None:
            result['RuleCategory'] = self.rule_category

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.warn_level is not None:
            result['WarnLevel'] = self.warn_level

        if self.warn_level_name is not None:
            result['WarnLevelName'] = self.warn_level_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')

        if m.get('ClientUa') is not None:
            self.client_ua = m.get('ClientUa')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataSet') is not None:
            self.data_set = m.get('DataSet')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EffectRow') is not None:
            self.effect_row = m.get('EffectRow')

        if m.get('ExecuteStatus') is not None:
            self.execute_status = m.get('ExecuteStatus')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('InWhiteList') is not None:
            self.in_white_list = m.get('InWhiteList')

        if m.get('InstanceAuditStatus') is not None:
            self.instance_audit_status = m.get('InstanceAuditStatus')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')

        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')

        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('OssObjectKey') is not None:
            self.oss_object_key = m.get('OssObjectKey')

        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RuleCategory') is not None:
            self.rule_category = m.get('RuleCategory')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('WarnLevel') is not None:
            self.warn_level = m.get('WarnLevel')

        if m.get('WarnLevelName') is not None:
            self.warn_level_name = m.get('WarnLevelName')

        return self

