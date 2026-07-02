# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAuditLogsRequest(DaraModel):
    def __init__(
        self,
        async_request_id: str = None,
        client_ip: str = None,
        client_ua: str = None,
        current_page: int = None,
        database_name: str = None,
        effect_row_range: str = None,
        end_time: int = None,
        execute_time_range: str = None,
        instance_name: str = None,
        ip_type: str = None,
        lang: str = None,
        load_white_list: bool = None,
        log_query_op_json: str = None,
        log_source: str = None,
        member_account: str = None,
        message: str = None,
        operate_type: str = None,
        oss_object_key: str = None,
        page_size: int = None,
        product_code: str = None,
        product_id: int = None,
        rule_agg_query: bool = None,
        rule_category: str = None,
        rule_id: str = None,
        rule_name: str = None,
        sql_text: str = None,
        start_time: int = None,
        user_name: str = None,
    ):
        # The request ID.
        self.async_request_id = async_request_id
        # The IP address of the request client.
        self.client_ip = client_ip
        # The client type.
        self.client_ua = client_ua
        # The page number in a paged query. Default value: 1.
        self.current_page = current_page
        # The database name.
        self.database_name = database_name
        # The range of affected rows.
        self.effect_row_range = effect_row_range
        # The end time of the alert log. The value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The range of execution time.
        self.execute_time_range = execute_time_range
        # The name of the asset instance.
        self.instance_name = instance_name
        # The network type. Valid values:
        # 
        # - **default** (default): non-Alibaba Cloud service
        # 
        # - **aliyun**: Alibaba Cloud service
        self.ip_type = ip_type
        # The language of the request and response. Default value: **zh_cn**. Valid values:
        # - **zh_cn**: Chinese.
        # - **en_us**: English.
        self.lang = lang
        # Specifies whether to load the whitelist status.
        self.load_white_list = load_white_list
        # The JSON string that specifies whether the query conditions are included.
        self.log_query_op_json = log_query_op_json
        # The data source.
        self.log_source = log_source
        # The UID of the member accounts.
        self.member_account = member_account
        # The message content.
        self.message = message
        # The operation type.
        self.operate_type = operate_type
        # The key of the OSS object.
        self.oss_object_key = oss_object_key
        # The number of entries per page in a paged query. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The name of the product to which the data asset belongs. Valid values: **MaxCompute, OSS, ADS, OTS, RDS**, and more.
        self.product_code = product_code
        # The ID that corresponds to the product name to which the data object belongs. Valid values:
        # - **1**: MaxCompute
        # - **2**: OSS
        # - **3**: ADB-MYSQL
        # - **4**: TableStore
        # - **5**: RDS
        # - **6**: SELF_DB
        # - **7**: PolarDB-X
        # - **8**: PolarDB
        # - **9**: ADB-PG
        # - **10**: OceanBase
        # - **11**: MongoDB
        # - **25**: Redis
        self.product_id = product_id
        # Specifies whether to perform an aggregate query.
        self.rule_agg_query = rule_agg_query
        # The rule type.
        self.rule_category = rule_category
        # The ID of the audit policy.
        self.rule_id = rule_id
        # The name of the audit policy.
        self.rule_name = rule_name
        # The content of the SQL statement.
        self.sql_text = sql_text
        # The start time of the alert log, in milliseconds.
        self.start_time = start_time
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_request_id is not None:
            result['AsyncRequestId'] = self.async_request_id

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_ua is not None:
            result['ClientUa'] = self.client_ua

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.effect_row_range is not None:
            result['EffectRowRange'] = self.effect_row_range

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.execute_time_range is not None:
            result['ExecuteTimeRange'] = self.execute_time_range

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.load_white_list is not None:
            result['LoadWhiteList'] = self.load_white_list

        if self.log_query_op_json is not None:
            result['LogQueryOpJson'] = self.log_query_op_json

        if self.log_source is not None:
            result['LogSource'] = self.log_source

        if self.member_account is not None:
            result['MemberAccount'] = self.member_account

        if self.message is not None:
            result['Message'] = self.message

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.oss_object_key is not None:
            result['OssObjectKey'] = self.oss_object_key

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.rule_agg_query is not None:
            result['RuleAggQuery'] = self.rule_agg_query

        if self.rule_category is not None:
            result['RuleCategory'] = self.rule_category

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncRequestId') is not None:
            self.async_request_id = m.get('AsyncRequestId')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientUa') is not None:
            self.client_ua = m.get('ClientUa')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EffectRowRange') is not None:
            self.effect_row_range = m.get('EffectRowRange')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecuteTimeRange') is not None:
            self.execute_time_range = m.get('ExecuteTimeRange')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LoadWhiteList') is not None:
            self.load_white_list = m.get('LoadWhiteList')

        if m.get('LogQueryOpJson') is not None:
            self.log_query_op_json = m.get('LogQueryOpJson')

        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')

        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('OssObjectKey') is not None:
            self.oss_object_key = m.get('OssObjectKey')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RuleAggQuery') is not None:
            self.rule_agg_query = m.get('RuleAggQuery')

        if m.get('RuleCategory') is not None:
            self.rule_category = m.get('RuleCategory')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

