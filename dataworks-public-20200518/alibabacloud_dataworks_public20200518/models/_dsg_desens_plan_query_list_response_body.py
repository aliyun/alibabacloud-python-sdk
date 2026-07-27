# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgDesensPlanQueryListResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        page_data: main_models.DsgDesensPlanQueryListResponseBodyPageData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The paginated data.
        self.page_data = page_data
        # The request ID. You can use this ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - true: The request was successful.
        # 
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.page_data:
            self.page_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_data is not None:
            result['PageData'] = self.page_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageData') is not None:
            temp_model = main_models.DsgDesensPlanQueryListResponseBodyPageData()
            self.page_data = temp_model.from_map(m.get('PageData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DsgDesensPlanQueryListResponseBodyPageData(DaraModel):
    def __init__(
        self,
        data: List[main_models.DsgDesensPlanQueryListResponseBodyPageDataData] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The details of the desensitization rules.
        self.data = data
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size
        # The total number of matching desensitization rules.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DsgDesensPlanQueryListResponseBodyPageDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DsgDesensPlanQueryListResponseBodyPageDataData(DaraModel):
    def __init__(
        self,
        check_watermark: bool = None,
        data_type: str = None,
        desen_mode: str = None,
        desens_plan: main_models.DsgDesensPlanQueryListResponseBodyPageDataDataDesensPlan = None,
        desens_rule: str = None,
        desens_way: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        owner: str = None,
        rule_name: str = None,
        scene_code: str = None,
        scene_name: str = None,
        status: int = None,
        columns: List[main_models.DsgDesensPlanQueryListResponseBodyPageDataDataColumns] = None,
        empty_not_desesn: bool = None,
    ):
        # Indicates whether to add a watermark. Valid values:
        # 
        # - true: A watermark is added.
        # 
        # - false: No watermark is added.
        self.check_watermark = check_watermark
        # The sensitive data type.
        self.data_type = data_type
        # The desensitization method.
        self.desen_mode = desen_mode
        # The details of the desensitization plan.
        self.desens_plan = desens_plan
        # The desensitization rule.
        self.desens_rule = desens_rule
        # The desensitization method.
        self.desens_way = desens_way
        # The time when the rule was created.
        self.gmt_create = gmt_create
        # The time when the rule was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the desensitization rule.
        self.id = id
        # The owner of the desensitization rule.
        self.owner = owner
        # The name of the desensitization rule.
        self.rule_name = rule_name
        # The level-1 desensitization scene code. Valid values:
        # 
        # - Desensitization for display in Data Development and Data Map: dataworks_display_desense_code
        # 
        # - Desensitization at the MaxCompute engine layer: maxcompute_desense_code
        # 
        # - Desensitization at the MaxCompute engine layer (New): maxcompute_new_desense_code
        # 
        # - Desensitization at the Hologres engine layer: hologres_display_desense_code
        # 
        # - Static desensitization in Data Integration: dataworks_data_integration_desense_code
        # 
        # - Desensitization for display in Data Analysis: dataworks_analysis_desense_code
        self.scene_code = scene_code
        # The name of the level-2 desensitization scene.
        self.scene_name = scene_name
        # The status of the rule. Valid values:
        # 
        # - 0: Inactive.
        # 
        # - 1: Active.
        self.status = status
        self.columns = columns
        self.empty_not_desesn = empty_not_desesn

    def validate(self):
        if self.desens_plan:
            self.desens_plan.validate()
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_watermark is not None:
            result['CheckWatermark'] = self.check_watermark

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.desen_mode is not None:
            result['DesenMode'] = self.desen_mode

        if self.desens_plan is not None:
            result['DesensPlan'] = self.desens_plan.to_map()

        if self.desens_rule is not None:
            result['DesensRule'] = self.desens_rule

        if self.desens_way is not None:
            result['DesensWay'] = self.desens_way

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.status is not None:
            result['Status'] = self.status

        result['columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['columns'].append(k1.to_map() if k1 else None)

        if self.empty_not_desesn is not None:
            result['emptyNotDesesn'] = self.empty_not_desesn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckWatermark') is not None:
            self.check_watermark = m.get('CheckWatermark')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DesenMode') is not None:
            self.desen_mode = m.get('DesenMode')

        if m.get('DesensPlan') is not None:
            temp_model = main_models.DsgDesensPlanQueryListResponseBodyPageDataDataDesensPlan()
            self.desens_plan = temp_model.from_map(m.get('DesensPlan'))

        if m.get('DesensRule') is not None:
            self.desens_rule = m.get('DesensRule')

        if m.get('DesensWay') is not None:
            self.desens_way = m.get('DesensWay')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.columns = []
        if m.get('columns') is not None:
            for k1 in m.get('columns'):
                temp_model = main_models.DsgDesensPlanQueryListResponseBodyPageDataDataColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('emptyNotDesesn') is not None:
            self.empty_not_desesn = m.get('emptyNotDesesn')

        return self

class DsgDesensPlanQueryListResponseBodyPageDataDataColumns(DaraModel):
    def __init__(
        self,
        column: str = None,
        db_type: str = None,
        project: str = None,
        table: str = None,
    ):
        self.column = column
        self.db_type = db_type
        self.project = project
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['column'] = self.column

        if self.db_type is not None:
            result['dbType'] = self.db_type

        if self.project is not None:
            result['project'] = self.project

        if self.table is not None:
            result['table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('column') is not None:
            self.column = m.get('column')

        if m.get('dbType') is not None:
            self.db_type = m.get('dbType')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('table') is not None:
            self.table = m.get('table')

        return self

class DsgDesensPlanQueryListResponseBodyPageDataDataDesensPlan(DaraModel):
    def __init__(
        self,
        desens_plan_type: str = None,
        ext_param: Dict[str, Any] = None,
    ):
        # The type of the desensitization plan.
        self.desens_plan_type = desens_plan_type
        # The parameters for the desensitization rule. For details, see the [DsgDesensPlanAddOrUpdate](https://help.aliyun.com/document_detail/2786295.html) operation.
        self.ext_param = ext_param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desens_plan_type is not None:
            result['DesensPlanType'] = self.desens_plan_type

        if self.ext_param is not None:
            result['ExtParam'] = self.ext_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesensPlanType') is not None:
            self.desens_plan_type = m.get('DesensPlanType')

        if m.get('ExtParam') is not None:
            self.ext_param = m.get('ExtParam')

        return self

