# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetLogListRequest(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        client_ip_list: List[str] = None,
        client_program_list: List[str] = None,
        db_host_list: List[str] = None,
        db_id: int = None,
        db_user_list: List[str] = None,
        end_date: str = None,
        instance_id: str = None,
        is_success: str = None,
        lang: str = None,
        max_affect_rows: int = None,
        max_exec_cost_us: int = None,
        min_affect_rows: int = None,
        min_exec_cost_us: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        risk_level_list: List[str] = None,
        rule_name: str = None,
        rule_type_list: List[str] = None,
        session_id: str = None,
        sql_id: str = None,
        sql_key: str = None,
        sql_type_list: List[str] = None,
        template_id: str = None,
    ):
        # This parameter is required.
        self.begin_date = begin_date
        self.client_ip_list = client_ip_list
        self.client_program_list = client_program_list
        self.db_host_list = db_host_list
        self.db_id = db_id
        self.db_user_list = db_user_list
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.instance_id = instance_id
        self.is_success = is_success
        self.lang = lang
        self.max_affect_rows = max_affect_rows
        self.max_exec_cost_us = max_exec_cost_us
        self.min_affect_rows = min_affect_rows
        self.min_exec_cost_us = min_exec_cost_us
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.risk_level_list = risk_level_list
        self.rule_name = rule_name
        self.rule_type_list = rule_type_list
        self.session_id = session_id
        self.sql_id = sql_id
        self.sql_key = sql_key
        self.sql_type_list = sql_type_list
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.client_ip_list is not None:
            result['ClientIpList'] = self.client_ip_list

        if self.client_program_list is not None:
            result['ClientProgramList'] = self.client_program_list

        if self.db_host_list is not None:
            result['DbHostList'] = self.db_host_list

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_user_list is not None:
            result['DbUserList'] = self.db_user_list

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_affect_rows is not None:
            result['MaxAffectRows'] = self.max_affect_rows

        if self.max_exec_cost_us is not None:
            result['MaxExecCostUS'] = self.max_exec_cost_us

        if self.min_affect_rows is not None:
            result['MinAffectRows'] = self.min_affect_rows

        if self.min_exec_cost_us is not None:
            result['MinExecCostUS'] = self.min_exec_cost_us

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type_list is not None:
            result['RuleTypeList'] = self.rule_type_list

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_key is not None:
            result['SqlKey'] = self.sql_key

        if self.sql_type_list is not None:
            result['SqlTypeList'] = self.sql_type_list

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('ClientIpList') is not None:
            self.client_ip_list = m.get('ClientIpList')

        if m.get('ClientProgramList') is not None:
            self.client_program_list = m.get('ClientProgramList')

        if m.get('DbHostList') is not None:
            self.db_host_list = m.get('DbHostList')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbUserList') is not None:
            self.db_user_list = m.get('DbUserList')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxAffectRows') is not None:
            self.max_affect_rows = m.get('MaxAffectRows')

        if m.get('MaxExecCostUS') is not None:
            self.max_exec_cost_us = m.get('MaxExecCostUS')

        if m.get('MinAffectRows') is not None:
            self.min_affect_rows = m.get('MinAffectRows')

        if m.get('MinExecCostUS') is not None:
            self.min_exec_cost_us = m.get('MinExecCostUS')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleTypeList') is not None:
            self.rule_type_list = m.get('RuleTypeList')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlKey') is not None:
            self.sql_key = m.get('SqlKey')

        if m.get('SqlTypeList') is not None:
            self.sql_type_list = m.get('SqlTypeList')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

