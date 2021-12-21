# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class DeleteAppExpMetricRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # APP ID
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppExpMetricRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppExpMetricRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAppExpMetricRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAppExpMetricRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppFollowCallRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # APP ID
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppFollowCallRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppFollowCallRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAppFollowCallRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAppFollowCallRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # APP ID
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeAppConfigResponseBodyThresholdConfig(TeaModel):
    def __init__(
        self,
        join_slow_time: int = None,
    ):
        # 入会慢时间阈值，单位毫秒
        self.join_slow_time = join_slow_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_slow_time is not None:
            result['JoinSlowTime'] = self.join_slow_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinSlowTime') is not None:
            self.join_slow_time = m.get('JoinSlowTime')
        return self


class DescribeAppConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        threshold_config: DescribeAppConfigResponseBodyThresholdConfig = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 阈值配置对象
        self.threshold_config = threshold_config

    def validate(self):
        if self.threshold_config:
            self.threshold_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.threshold_config is not None:
            result['ThresholdConfig'] = self.threshold_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ThresholdConfig') is not None:
            temp_model = DescribeAppConfigResponseBodyThresholdConfig()
            self.threshold_config = temp_model.from_map(m['ThresholdConfig'])
        return self


class DescribeAppConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppExpMetricRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # APP ID
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeAppExpMetricRuleResponseBodyAppExpMetricRule(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        created_ts: int = None,
        gmt_create_ts: int = None,
        gmt_modified_ts: int = None,
        modified_ts: int = None,
        rule: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 创建时间，秒级时间戳，如1614912647
        self.created_ts = created_ts
        self.gmt_create_ts = gmt_create_ts
        self.gmt_modified_ts = gmt_modified_ts
        # 修改时间，秒级时间戳，如1615272998
        self.modified_ts = modified_ts
        # 具体规则，JSON格式
        self.rule = rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.gmt_create_ts is not None:
            result['GmtCreateTs'] = self.gmt_create_ts
        if self.gmt_modified_ts is not None:
            result['GmtModifiedTs'] = self.gmt_modified_ts
        if self.modified_ts is not None:
            result['ModifiedTs'] = self.modified_ts
        if self.rule is not None:
            result['Rule'] = self.rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('GmtCreateTs') is not None:
            self.gmt_create_ts = m.get('GmtCreateTs')
        if m.get('GmtModifiedTs') is not None:
            self.gmt_modified_ts = m.get('GmtModifiedTs')
        if m.get('ModifiedTs') is not None:
            self.modified_ts = m.get('ModifiedTs')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        return self


class DescribeAppExpMetricRuleResponseBody(TeaModel):
    def __init__(
        self,
        app_exp_metric_rule: DescribeAppExpMetricRuleResponseBodyAppExpMetricRule = None,
        request_id: str = None,
    ):
        # 获取用户体验阈值规则相关数据
        self.app_exp_metric_rule = app_exp_metric_rule
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.app_exp_metric_rule:
            self.app_exp_metric_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_exp_metric_rule is not None:
            result['AppExpMetricRule'] = self.app_exp_metric_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppExpMetricRule') is not None:
            temp_model = DescribeAppExpMetricRuleResponseBodyAppExpMetricRule()
            self.app_exp_metric_rule = temp_model.from_map(m['AppExpMetricRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppExpMetricRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppExpMetricRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppExpMetricRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppExpMetricRuleListResponseBodyAppExpMetricRuleList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        created_ts: int = None,
        gmt_create_ts: int = None,
        gmt_modified_ts: int = None,
        modified_ts: int = None,
        rule: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 创建时间，秒级时间戳，如1614912647
        self.created_ts = created_ts
        self.gmt_create_ts = gmt_create_ts
        self.gmt_modified_ts = gmt_modified_ts
        # 修改时间，秒级时间戳，如1615272998
        self.modified_ts = modified_ts
        # 具体规则，JSON格式
        self.rule = rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.gmt_create_ts is not None:
            result['GmtCreateTs'] = self.gmt_create_ts
        if self.gmt_modified_ts is not None:
            result['GmtModifiedTs'] = self.gmt_modified_ts
        if self.modified_ts is not None:
            result['ModifiedTs'] = self.modified_ts
        if self.rule is not None:
            result['Rule'] = self.rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('GmtCreateTs') is not None:
            self.gmt_create_ts = m.get('GmtCreateTs')
        if m.get('GmtModifiedTs') is not None:
            self.gmt_modified_ts = m.get('GmtModifiedTs')
        if m.get('ModifiedTs') is not None:
            self.modified_ts = m.get('ModifiedTs')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        return self


class DescribeAppExpMetricRuleListResponseBody(TeaModel):
    def __init__(
        self,
        app_exp_metric_rule_list: List[DescribeAppExpMetricRuleListResponseBodyAppExpMetricRuleList] = None,
        request_id: str = None,
    ):
        # 用户体验阈值规则相关数据列表
        self.app_exp_metric_rule_list = app_exp_metric_rule_list
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.app_exp_metric_rule_list:
            for k in self.app_exp_metric_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppExpMetricRuleList'] = []
        if self.app_exp_metric_rule_list is not None:
            for k in self.app_exp_metric_rule_list:
                result['AppExpMetricRuleList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_exp_metric_rule_list = []
        if m.get('AppExpMetricRuleList') is not None:
            for k in m.get('AppExpMetricRuleList'):
                temp_model = DescribeAppExpMetricRuleListResponseBodyAppExpMetricRuleList()
                self.app_exp_metric_rule_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppExpMetricRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppExpMetricRuleListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppExpMetricRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppFollowCallRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # APP ID
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeAppFollowCallRuleResponseBodyAppFollowCallRule(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        created_ts: int = None,
        gmt_create_ts: int = None,
        gmt_modified_ts: int = None,
        modified_ts: int = None,
        rule: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 创建时间，秒级时间戳，如1614936817
        self.created_ts = created_ts
        self.gmt_create_ts = gmt_create_ts
        self.gmt_modified_ts = gmt_modified_ts
        # 修改时间，秒级时间戳，如1614936817
        self.modified_ts = modified_ts
        # 具体规则，JSON格式
        self.rule = rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.gmt_create_ts is not None:
            result['GmtCreateTs'] = self.gmt_create_ts
        if self.gmt_modified_ts is not None:
            result['GmtModifiedTs'] = self.gmt_modified_ts
        if self.modified_ts is not None:
            result['ModifiedTs'] = self.modified_ts
        if self.rule is not None:
            result['Rule'] = self.rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('GmtCreateTs') is not None:
            self.gmt_create_ts = m.get('GmtCreateTs')
        if m.get('GmtModifiedTs') is not None:
            self.gmt_modified_ts = m.get('GmtModifiedTs')
        if m.get('ModifiedTs') is not None:
            self.modified_ts = m.get('ModifiedTs')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        return self


class DescribeAppFollowCallRuleResponseBody(TeaModel):
    def __init__(
        self,
        app_follow_call_rule: DescribeAppFollowCallRuleResponseBodyAppFollowCallRule = None,
        request_id: str = None,
    ):
        # 获取用户体验阈值规则相关数据
        self.app_follow_call_rule = app_follow_call_rule
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.app_follow_call_rule:
            self.app_follow_call_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_follow_call_rule is not None:
            result['AppFollowCallRule'] = self.app_follow_call_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppFollowCallRule') is not None:
            temp_model = DescribeAppFollowCallRuleResponseBodyAppFollowCallRule()
            self.app_follow_call_rule = temp_model.from_map(m['AppFollowCallRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppFollowCallRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppFollowCallRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppFollowCallRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppFollowCallRuleListResponseBodyAppFollowCallRuleList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        created_ts: int = None,
        gmt_create_ts: int = None,
        gmt_modified_ts: int = None,
        modified_ts: int = None,
        rule: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # 创建时间，秒级时间戳，如1614836732
        self.created_ts = created_ts
        # 创建时间，待删除
        self.gmt_create_ts = gmt_create_ts
        # 修改时间，待删除
        self.gmt_modified_ts = gmt_modified_ts
        # 修改时间，秒级时间戳，如1614836732
        self.modified_ts = modified_ts
        # 具体规则，JSON格式
        self.rule = rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.gmt_create_ts is not None:
            result['GmtCreateTs'] = self.gmt_create_ts
        if self.gmt_modified_ts is not None:
            result['GmtModifiedTs'] = self.gmt_modified_ts
        if self.modified_ts is not None:
            result['ModifiedTs'] = self.modified_ts
        if self.rule is not None:
            result['Rule'] = self.rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('GmtCreateTs') is not None:
            self.gmt_create_ts = m.get('GmtCreateTs')
        if m.get('GmtModifiedTs') is not None:
            self.gmt_modified_ts = m.get('GmtModifiedTs')
        if m.get('ModifiedTs') is not None:
            self.modified_ts = m.get('ModifiedTs')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        return self


class DescribeAppFollowCallRuleListResponseBody(TeaModel):
    def __init__(
        self,
        app_follow_call_rule_list: List[DescribeAppFollowCallRuleListResponseBodyAppFollowCallRuleList] = None,
        request_id: str = None,
    ):
        # 通信监测关注规则相关数据列表
        self.app_follow_call_rule_list = app_follow_call_rule_list
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.app_follow_call_rule_list:
            for k in self.app_follow_call_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppFollowCallRuleList'] = []
        if self.app_follow_call_rule_list is not None:
            for k in self.app_follow_call_rule_list:
                result['AppFollowCallRuleList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_follow_call_rule_list = []
        if m.get('AppFollowCallRuleList') is not None:
            for k in m.get('AppFollowCallRuleList'):
                temp_model = DescribeAppFollowCallRuleListResponseBodyAppFollowCallRuleList()
                self.app_follow_call_rule_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppFollowCallRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppFollowCallRuleListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppFollowCallRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        ext_data_type: str = None,
        query_exp_info: bool = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID。
        self.channel_id = channel_id
        # 创建频道时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 频道释放时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts
        # 查询的扩展。取值：USER_DURATION_STAT：用户时长统计数据类型。
        self.ext_data_type = ext_data_type
        # 是否查询通信体验信息，不传默认是true
        self.query_exp_info = query_exp_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.ext_data_type is not None:
            result['ExtDataType'] = self.ext_data_type
        if self.query_exp_info is not None:
            result['QueryExpInfo'] = self.query_exp_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('ExtDataType') is not None:
            self.ext_data_type = m.get('ExtDataType')
        if m.get('QueryExpInfo') is not None:
            self.query_exp_info = m.get('QueryExpInfo')
        return self


class DescribeCallResponseBodyCallInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
    ):
        # App ID。
        self.app_id = app_id
        # 通信状态。取值：IN：进行中。OUT：已结束。
        self.call_status = call_status
        # 频道ID。
        self.channel_id = channel_id
        # 创建通信时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 释放通信时间，使用UNIX时间戳表示，单位：秒。
        self.destroyed_ts = destroyed_ts
        # 通信持续时长，单位：秒。
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeCallResponseBodyUserDetailListDurMetricStatData(TeaModel):
    def __init__(
        self,
        pub_audio: int = None,
        pub_video_1080: int = None,
        pub_video_360: int = None,
        pub_video_720: int = None,
        pub_video_screen_share: int = None,
        sub_audio: int = None,
        sub_video_1080: int = None,
        sub_video_360: int = None,
        sub_video_720: int = None,
        sub_video_screen_share: int = None,
    ):
        # 发布音频时长，单位秒
        self.pub_audio = pub_audio
        # 发布1080P视频时长，单位：秒
        self.pub_video_1080 = pub_video_1080
        # 发布360P视频时长，单位秒
        self.pub_video_360 = pub_video_360
        # 发布720P视频时长，单位：秒
        self.pub_video_720 = pub_video_720
        # 发布屏幕共享时长，单位：秒
        self.pub_video_screen_share = pub_video_screen_share
        # 订阅音频时长，单位秒
        self.sub_audio = sub_audio
        # 订阅1080P视频时长，单位：秒
        self.sub_video_1080 = sub_video_1080
        # 订阅360P视频时长，单位：秒
        self.sub_video_360 = sub_video_360
        # 订阅720P视频时长，单位：秒
        self.sub_video_720 = sub_video_720
        # 订阅屏幕共享时长，单位：秒
        self.sub_video_screen_share = sub_video_screen_share

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pub_audio is not None:
            result['PubAudio'] = self.pub_audio
        if self.pub_video_1080 is not None:
            result['PubVideo1080'] = self.pub_video_1080
        if self.pub_video_360 is not None:
            result['PubVideo360'] = self.pub_video_360
        if self.pub_video_720 is not None:
            result['PubVideo720'] = self.pub_video_720
        if self.pub_video_screen_share is not None:
            result['PubVideoScreenShare'] = self.pub_video_screen_share
        if self.sub_audio is not None:
            result['SubAudio'] = self.sub_audio
        if self.sub_video_1080 is not None:
            result['SubVideo1080'] = self.sub_video_1080
        if self.sub_video_360 is not None:
            result['SubVideo360'] = self.sub_video_360
        if self.sub_video_720 is not None:
            result['SubVideo720'] = self.sub_video_720
        if self.sub_video_screen_share is not None:
            result['SubVideoScreenShare'] = self.sub_video_screen_share
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PubAudio') is not None:
            self.pub_audio = m.get('PubAudio')
        if m.get('PubVideo1080') is not None:
            self.pub_video_1080 = m.get('PubVideo1080')
        if m.get('PubVideo360') is not None:
            self.pub_video_360 = m.get('PubVideo360')
        if m.get('PubVideo720') is not None:
            self.pub_video_720 = m.get('PubVideo720')
        if m.get('PubVideoScreenShare') is not None:
            self.pub_video_screen_share = m.get('PubVideoScreenShare')
        if m.get('SubAudio') is not None:
            self.sub_audio = m.get('SubAudio')
        if m.get('SubVideo1080') is not None:
            self.sub_video_1080 = m.get('SubVideo1080')
        if m.get('SubVideo360') is not None:
            self.sub_video_360 = m.get('SubVideo360')
        if m.get('SubVideo720') is not None:
            self.sub_video_720 = m.get('SubVideo720')
        if m.get('SubVideoScreenShare') is not None:
            self.sub_video_screen_share = m.get('SubVideoScreenShare')
        return self


class DescribeCallResponseBodyUserDetailListOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        # 加入通话时间，使用UNIX时间戳表示，单位：秒。
        self.join_ts = join_ts
        # 离开通话时间，使用UNIX时间戳表示，单位：秒。
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribeCallResponseBodyUserDetailList(TeaModel):
    def __init__(
        self,
        call_exp: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        dur_metric_stat_data: DescribeCallResponseBodyUserDetailListDurMetricStatData = None,
        duration: int = None,
        location: str = None,
        network: str = None,
        network_list: List[str] = None,
        online_duration: int = None,
        online_periods: List[DescribeCallResponseBodyUserDetailListOnlinePeriods] = None,
        os: str = None,
        os_list: List[str] = None,
        roles: List[str] = None,
        sdk_version: str = None,
        sdk_version_list: List[str] = None,
        user_id: str = None,
        user_id_alias: str = None,
    ):
        # 通话体验，取值：GOOD:优良，BAD:欠佳。
        self.call_exp = call_exp
        # 创建通话时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 释放通话时间，使用UNIX时间戳表示，单位：秒。通话未结束时值为0。
        self.destroyed_ts = destroyed_ts
        # 时长统计数据
        self.dur_metric_stat_data = dur_metric_stat_data
        # 通话时长，首次进入到最后离开，单位：秒。
        self.duration = duration
        # 地理位置信息，例如：北京市-北京市
        self.location = location
        # 网络类型，如WiFi，4G等
        self.network = network
        # 网络类型，如WiFi，4G等
        self.network_list = network_list
        # 在线时长，单位：秒。
        self.online_duration = online_duration
        # 在线时段信息。
        self.online_periods = online_periods
        # 平台类型：若用户客户端为WEB则是浏览器类型，若客户端为NATIVE则是操作系统类型
        self.os = os
        # 平台类型：若用户客户端为WEB则是浏览器类型，若客户端为NATIVE则是操作系统类型
        self.os_list = os_list
        # 用户角色，取值：SENDER：发布端。RECEIVER：订阅端。
        self.roles = roles
        # SDK版本，如1.0.0、1.1.1等
        self.sdk_version = sdk_version
        # SDK版本列表，如1.0.0、1.1.1等
        self.sdk_version_list = sdk_version_list
        # 用户ID。
        self.user_id = user_id
        # 用户ID 别称
        self.user_id_alias = user_id_alias

    def validate(self):
        if self.dur_metric_stat_data:
            self.dur_metric_stat_data.validate()
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_exp is not None:
            result['CallExp'] = self.call_exp
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.dur_metric_stat_data is not None:
            result['DurMetricStatData'] = self.dur_metric_stat_data.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.network_list is not None:
            result['NetworkList'] = self.network_list
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.os_list is not None:
            result['OsList'] = self.os_list
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sdk_version_list is not None:
            result['SdkVersionList'] = self.sdk_version_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_id_alias is not None:
            result['UserIdAlias'] = self.user_id_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallExp') is not None:
            self.call_exp = m.get('CallExp')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('DurMetricStatData') is not None:
            temp_model = DescribeCallResponseBodyUserDetailListDurMetricStatData()
            self.dur_metric_stat_data = temp_model.from_map(m['DurMetricStatData'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NetworkList') is not None:
            self.network_list = m.get('NetworkList')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribeCallResponseBodyUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsList') is not None:
            self.os_list = m.get('OsList')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('SdkVersionList') is not None:
            self.sdk_version_list = m.get('SdkVersionList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')
        return self


class DescribeCallResponseBody(TeaModel):
    def __init__(
        self,
        call_info: DescribeCallResponseBodyCallInfo = None,
        request_id: str = None,
        user_detail_list: List[DescribeCallResponseBodyUserDetailList] = None,
    ):
        # 通信基本信息。
        self.call_info = call_info
        # 请求ID
        self.request_id = request_id
        # 用户详情列表。
        self.user_detail_list = user_detail_list

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.user_detail_list:
            for k in self.user_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserDetailList'] = []
        if self.user_detail_list is not None:
            for k in self.user_detail_list:
                result['UserDetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = DescribeCallResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m['CallInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_detail_list = []
        if m.get('UserDetailList') is not None:
            for k in m.get('UserDetailList'):
                temp_model = DescribeCallResponseBodyUserDetailList()
                self.user_detail_list.append(temp_model.from_map(k))
        return self


class DescribeCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCallResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        end_ts: int = None,
        order_by: str = None,
        page_no: int = None,
        page_size: int = None,
        query_mode: str = None,
        start_ts: int = None,
        user_id: str = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 通信状态。取值：IN：进行中。OUT：已结束。
        self.call_status = call_status
        # 频道ID
        self.channel_id = channel_id
        # 查询的结束时间，使用UNIX时间戳表示，单位：秒。
        self.end_ts = end_ts
        # 排序字段。取值：BAD_EXP_USER_COUNT_DESC：按体验欠佳人数降序。BAD_EXP_USER_COUNT_ASC：按体验欠佳人数升序
        self.order_by = order_by
        # 页码
        self.page_no = page_no
        # 每页数量
        self.page_size = page_size
        # 查询模式。取值：ALL：全部通话。FOLLOW：关注通话。
        self.query_mode = query_mode
        # 查询的开始时间，使用UNIX时间戳表示，单位：秒。
        self.start_ts = start_ts
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeCallListResponseBodyCallList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        bad_exp_user_cnt: int = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        user_cnt: int = None,
    ):
        # App ID。
        self.app_id = app_id
        # 通信体验差的用户数。
        self.bad_exp_user_cnt = bad_exp_user_cnt
        # 通信状态，IN：进行中，OUT：已结束
        self.call_status = call_status
        # 频道ID。
        self.channel_id = channel_id
        # 通信的创建时间戳，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 通信的释放时间戳，使用UNIX时间戳表示，单位：秒。
        self.destroyed_ts = destroyed_ts
        # 通信持续时长，单位：秒。
        self.duration = duration
        # 通信用户数。
        self.user_cnt = user_cnt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bad_exp_user_cnt is not None:
            result['BadExpUserCnt'] = self.bad_exp_user_cnt
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.user_cnt is not None:
            result['UserCnt'] = self.user_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BadExpUserCnt') is not None:
            self.bad_exp_user_cnt = m.get('BadExpUserCnt')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('UserCnt') is not None:
            self.user_cnt = m.get('UserCnt')
        return self


class DescribeCallListResponseBody(TeaModel):
    def __init__(
        self,
        call_list: List[DescribeCallListResponseBodyCallList] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
    ):
        # 通信列表。
        self.call_list = call_list
        # 页码。
        self.page_no = page_no
        # 每页数量。
        self.page_size = page_size
        # 请求ID。
        self.request_id = request_id
        # 总数量。
        self.total_cnt = total_cnt

    def validate(self):
        if self.call_list:
            for k in self.call_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CallList'] = []
        if self.call_list is not None:
            for k in self.call_list:
                result['CallList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_list = []
        if m.get('CallList') is not None:
            for k in m.get('CallList'):
                temp_model = DescribeCallListResponseBodyCallList()
                self.call_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        return self


class DescribeCallListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCallListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCallListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallListTestRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        start_ts: int = None,
    ):
        self.app_id = app_id
        self.end_ts = end_ts
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeCallListTestResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCallListTestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCallListTestResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCallListTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCallUserExpRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID。
        self.channel_id = channel_id
        # 创建频道时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 频道释放时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeCallUserExpResponseBodyExpInfoList(TeaModel):
    def __init__(
        self,
        call_exp: str = None,
        user_id: str = None,
    ):
        # 用户体验：GOOD:优良, BAD:欠佳
        self.call_exp = call_exp
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_exp is not None:
            result['CallExp'] = self.call_exp
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallExp') is not None:
            self.call_exp = m.get('CallExp')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeCallUserExpResponseBody(TeaModel):
    def __init__(
        self,
        exp_info_list: List[DescribeCallUserExpResponseBodyExpInfoList] = None,
        request_id: str = None,
    ):
        # 通信体验信息。
        self.exp_info_list = exp_info_list
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.exp_info_list:
            for k in self.exp_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExpInfoList'] = []
        if self.exp_info_list is not None:
            for k in self.exp_info_list:
                result['ExpInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exp_info_list = []
        if m.get('ExpInfoList') is not None:
            for k in m.get('ExpInfoList'):
                temp_model = DescribeCallUserExpResponseBodyExpInfoList()
                self.exp_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCallUserExpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCallUserExpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCallUserExpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelAreaDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        parent_area: str = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID
        self.channel_id = channel_id
        # 频道创建时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 频道释放时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts
        # 父级地区名称，例如：深圳市的父级为广东省。参数为空表示世界范围（国家维度）的统计，例如：中国、英国。
        self.parent_area = parent_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.parent_area is not None:
            result['ParentArea'] = self.parent_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('ParentArea') is not None:
            self.parent_area = m.get('ParentArea')
        return self


class DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList(TeaModel):
    def __init__(
        self,
        area_name: str = None,
        call_user_count: int = None,
        high_quality_transmission_rate: str = None,
        pub_user_count: int = None,
        sub_user_count: int = None,
    ):
        # 地域名称，例如：中国_浙江省_杭州市。
        self.area_name = area_name
        # 通信人数。
        self.call_user_count = call_user_count
        # 优质传输率，用小数表示，例如0.9999表示优质传输率为99.99%。
        self.high_quality_transmission_rate = high_quality_transmission_rate
        # 发布端人数。
        self.pub_user_count = pub_user_count
        # 订阅端人数。
        self.sub_user_count = sub_user_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.call_user_count is not None:
            result['CallUserCount'] = self.call_user_count
        if self.high_quality_transmission_rate is not None:
            result['HighQualityTransmissionRate'] = self.high_quality_transmission_rate
        if self.pub_user_count is not None:
            result['PubUserCount'] = self.pub_user_count
        if self.sub_user_count is not None:
            result['SubUserCount'] = self.sub_user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CallUserCount') is not None:
            self.call_user_count = m.get('CallUserCount')
        if m.get('HighQualityTransmissionRate') is not None:
            self.high_quality_transmission_rate = m.get('HighQualityTransmissionRate')
        if m.get('PubUserCount') is not None:
            self.pub_user_count = m.get('PubUserCount')
        if m.get('SubUserCount') is not None:
            self.sub_user_count = m.get('SubUserCount')
        return self


class DescribeChannelAreaDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        area_stat_list: List[DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList] = None,
        request_id: str = None,
    ):
        # 地域统计列表。
        self.area_stat_list = area_stat_list
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.area_stat_list:
            for k in self.area_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AreaStatList'] = []
        if self.area_stat_list is not None:
            for k in self.area_stat_list:
                result['AreaStatList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.area_stat_list = []
        if m.get('AreaStatList') is not None:
            for k in m.get('AreaStatList'):
                temp_model = DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList()
                self.area_stat_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelAreaDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChannelAreaDistributionStatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeChannelAreaDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        stat_dim: str = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID
        self.channel_id = channel_id
        # 创建频道的时间戳，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 频道释放时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts
        # 统计维度，取值：OS：按照系统统计。SDK_VERSION：按照SDK版本统计。
        self.stat_dim = stat_dim

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeChannelDistributionStatDataResponseBodyStatList(TeaModel):
    def __init__(
        self,
        call_user_count: int = None,
        call_user_ratio: str = None,
        name: str = None,
    ):
        # 通信人数。
        self.call_user_count = call_user_count
        # 通信人数占比，用小数表示，例如1.0000表示通信人数占比为100%。
        self.call_user_ratio = call_user_ratio
        # 统计维度。
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_user_count is not None:
            result['CallUserCount'] = self.call_user_count
        if self.call_user_ratio is not None:
            result['CallUserRatio'] = self.call_user_ratio
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallUserCount') is not None:
            self.call_user_count = m.get('CallUserCount')
        if m.get('CallUserRatio') is not None:
            self.call_user_ratio = m.get('CallUserRatio')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeChannelDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stat_list: List[DescribeChannelDistributionStatDataResponseBodyStatList] = None,
    ):
        # 请求ID。
        self.request_id = request_id
        # 频道分布统计列表。
        self.stat_list = stat_list

    def validate(self):
        if self.stat_list:
            for k in self.stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatList'] = []
        if self.stat_list is not None:
            for k in self.stat_list:
                result['StatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stat_list = []
        if m.get('StatList') is not None:
            for k in m.get('StatList'):
                temp_model = DescribeChannelDistributionStatDataResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k))
        return self


class DescribeChannelDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChannelDistributionStatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeChannelDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelJoinInfoRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        # APP ID
        self.app_id = app_id
        # 频道ID
        self.channel_id = channel_id
        # 频道创建时间
        self.created_ts = created_ts
        # 频道释放时间
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelJoinInfoResponseBody(TeaModel):
    def __init__(
        self,
        join_fast_success_rate: str = None,
        join_slow_threshold: int = None,
        request_id: str = None,
    ):
        # 在入会慢时间阈值内的入会成功率
        self.join_fast_success_rate = join_fast_success_rate
        # 入会慢时间阈值
        self.join_slow_threshold = join_slow_threshold
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_fast_success_rate is not None:
            result['JoinFastSuccessRate'] = self.join_fast_success_rate
        if self.join_slow_threshold is not None:
            result['JoinSlowThreshold'] = self.join_slow_threshold
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinFastSuccessRate') is not None:
            self.join_fast_success_rate = m.get('JoinFastSuccessRate')
        if m.get('JoinSlowThreshold') is not None:
            self.join_slow_threshold = m.get('JoinSlowThreshold')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelJoinInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChannelJoinInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeChannelJoinInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelOverallDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID。
        self.channel_id = channel_id
        # 创建频道的时间戳，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 频道释放时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelOverallDataResponseBodyCallInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
    ):
        # 应用ID。
        self.app_id = app_id
        # 通信状态，取值：IN：进行中。OUT：已结束
        self.call_status = call_status
        # 频道ID。
        self.channel_id = channel_id
        # 创建通信的时间戳，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 释放通信的时间戳，使用UNIX时间戳表示，单位：秒。
        self.destroyed_ts = destroyed_ts
        # 通信时长，单位：秒。
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeChannelOverallDataResponseBodyMetricDatasNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        # 扩展数据
        self.ext = ext
        # 指标趋势图中x轴横坐标。
        self.x = x
        # 指标趋势图中y轴纵坐标。
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeChannelOverallDataResponseBodyMetricDatas(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeChannelOverallDataResponseBodyMetricDatasNodes] = None,
        type: str = None,
    ):
        # 指标趋势图坐标点列表。
        self.nodes = nodes
        # 指标类型，取值：CALL_QUALITY：通信质量。CONN_NUM：通信次数。
        self.type = type

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeChannelOverallDataResponseBodyMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeChannelOverallDataResponseBodyOverallData(TeaModel):
    def __init__(
        self,
        conn_avg_time: float = None,
        five_sec_join_rate: float = None,
        total_audio_stuck_rate: float = None,
        total_video_stuck_rate: float = None,
        total_video_vague_rate: float = None,
    ):
        # 平均通信连接的用时，单位：秒。
        self.conn_avg_time = conn_avg_time
        # 5秒内连通成功率，用小数表示，例如1.0表示连通成功率为100%。
        self.five_sec_join_rate = five_sec_join_rate
        # 整体音频卡顿率，用小数表示，例如0.02表示音频卡顿率为2%。
        self.total_audio_stuck_rate = total_audio_stuck_rate
        # 整体视频卡顿率，用小数表示，例如0.02表示视频卡顿率为2%。
        self.total_video_stuck_rate = total_video_stuck_rate
        # 整体视频模糊率，用小数表示，例如0.02表示视频模糊率为2%。
        self.total_video_vague_rate = total_video_vague_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_avg_time is not None:
            result['ConnAvgTime'] = self.conn_avg_time
        if self.five_sec_join_rate is not None:
            result['FiveSecJoinRate'] = self.five_sec_join_rate
        if self.total_audio_stuck_rate is not None:
            result['TotalAudioStuckRate'] = self.total_audio_stuck_rate
        if self.total_video_stuck_rate is not None:
            result['TotalVideoStuckRate'] = self.total_video_stuck_rate
        if self.total_video_vague_rate is not None:
            result['TotalVideoVagueRate'] = self.total_video_vague_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAvgTime') is not None:
            self.conn_avg_time = m.get('ConnAvgTime')
        if m.get('FiveSecJoinRate') is not None:
            self.five_sec_join_rate = m.get('FiveSecJoinRate')
        if m.get('TotalAudioStuckRate') is not None:
            self.total_audio_stuck_rate = m.get('TotalAudioStuckRate')
        if m.get('TotalVideoStuckRate') is not None:
            self.total_video_stuck_rate = m.get('TotalVideoStuckRate')
        if m.get('TotalVideoVagueRate') is not None:
            self.total_video_vague_rate = m.get('TotalVideoVagueRate')
        return self


class DescribeChannelOverallDataResponseBody(TeaModel):
    def __init__(
        self,
        call_info: DescribeChannelOverallDataResponseBodyCallInfo = None,
        metric_datas: List[DescribeChannelOverallDataResponseBodyMetricDatas] = None,
        overall_data: DescribeChannelOverallDataResponseBodyOverallData = None,
        request_id: str = None,
    ):
        # 通信基本信息。
        self.call_info = call_info
        # 指标数据列表。
        self.metric_datas = metric_datas
        # 概览数据。
        self.overall_data = overall_data
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.metric_datas:
            for k in self.metric_datas:
                if k:
                    k.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()
        result['MetricDatas'] = []
        if self.metric_datas is not None:
            for k in self.metric_datas:
                result['MetricDatas'].append(k.to_map() if k else None)
        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = DescribeChannelOverallDataResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m['CallInfo'])
        self.metric_datas = []
        if m.get('MetricDatas') is not None:
            for k in m.get('MetricDatas'):
                temp_model = DescribeChannelOverallDataResponseBodyMetricDatas()
                self.metric_datas.append(temp_model.from_map(k))
        if m.get('OverallData') is not None:
            temp_model = DescribeChannelOverallDataResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m['OverallData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelOverallDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChannelOverallDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeChannelOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelTopPubUserListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID。
        self.channel_id = channel_id
        # 创建频道的时间戳，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 频道释放时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        # 加入通话时间，使用UNIX时间戳表示，单位：秒。
        self.join_ts = join_ts
        # 离开通话时间，使用UNIX时间戳表示，单位：秒。
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList(TeaModel):
    def __init__(
        self,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        location: str = None,
        online_duration: int = None,
        online_periods: List[DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods] = None,
        user_id: str = None,
    ):
        # 第一次加入通话的时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 最后一次离开通话的时间，使用UNIX时间戳表示，单位：秒。通话未结束时值为0。
        self.destroyed_ts = destroyed_ts
        # 总时长，单位：秒。
        self.duration = duration
        # 地域位置，例如：北京市-北京市
        self.location = location
        # 通信时长，单位：秒。
        self.online_duration = online_duration
        # 在线期间用户列表。
        self.online_periods = online_periods
        # 用户ID。
        self.user_id = user_id

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeChannelTopPubUserListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        top_pub_user_detail_list: List[DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList] = None,
    ):
        # 请求ID。
        self.request_id = request_id
        # Top发布用户详情列表
        self.top_pub_user_detail_list = top_pub_user_detail_list

    def validate(self):
        if self.top_pub_user_detail_list:
            for k in self.top_pub_user_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TopPubUserDetailList'] = []
        if self.top_pub_user_detail_list is not None:
            for k in self.top_pub_user_detail_list:
                result['TopPubUserDetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.top_pub_user_detail_list = []
        if m.get('TopPubUserDetailList') is not None:
            for k in m.get('TopPubUserDetailList'):
                temp_model = DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList()
                self.top_pub_user_detail_list.append(temp_model.from_map(k))
        return self


class DescribeChannelTopPubUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChannelTopPubUserListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeChannelTopPubUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChannelUserMetricsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID。
        self.channel_id = channel_id
        # 频道的创建时间戳，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 频道释放时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        return self


class DescribeChannelUserMetricsResponseBodyMetricDatasNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        # 拓展属性
        self.ext = ext
        # 指标趋势图中x轴横坐标。
        self.x = x
        # 指标趋势图中y轴纵坐标。
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeChannelUserMetricsResponseBodyMetricDatas(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeChannelUserMetricsResponseBodyMetricDatasNodes] = None,
        type: str = None,
    ):
        # 指标趋势图坐标点列表。
        self.nodes = nodes
        # 指标类型，取值：ALL_NUM：累计用户数量。PUB_NUM：累计发布用户数量。SUB_NUM：累计订阅用户数量。JOIN_FAIL_NUM：累计加入频道异常用户数量。BAD_EXP_NUM：累计通信体验异常用户。
        self.type = type

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeChannelUserMetricsResponseBodyMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeChannelUserMetricsResponseBodyOverallData(TeaModel):
    def __init__(
        self,
        total_bad_exp_num: int = None,
        total_join_fail_num: int = None,
        total_pub_user_num: int = None,
        total_sub_user_num: int = None,
        total_user_num: int = None,
    ):
        # 累计通信体验异常用户数量。
        self.total_bad_exp_num = total_bad_exp_num
        # 累计加入频道异常用户数量。
        self.total_join_fail_num = total_join_fail_num
        # 累计发布端用户数量。
        self.total_pub_user_num = total_pub_user_num
        # 累计订阅端用户数量。
        self.total_sub_user_num = total_sub_user_num
        # 累计用户数量。
        self.total_user_num = total_user_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_bad_exp_num is not None:
            result['TotalBadExpNum'] = self.total_bad_exp_num
        if self.total_join_fail_num is not None:
            result['TotalJoinFailNum'] = self.total_join_fail_num
        if self.total_pub_user_num is not None:
            result['TotalPubUserNum'] = self.total_pub_user_num
        if self.total_sub_user_num is not None:
            result['TotalSubUserNum'] = self.total_sub_user_num
        if self.total_user_num is not None:
            result['TotalUserNum'] = self.total_user_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalBadExpNum') is not None:
            self.total_bad_exp_num = m.get('TotalBadExpNum')
        if m.get('TotalJoinFailNum') is not None:
            self.total_join_fail_num = m.get('TotalJoinFailNum')
        if m.get('TotalPubUserNum') is not None:
            self.total_pub_user_num = m.get('TotalPubUserNum')
        if m.get('TotalSubUserNum') is not None:
            self.total_sub_user_num = m.get('TotalSubUserNum')
        if m.get('TotalUserNum') is not None:
            self.total_user_num = m.get('TotalUserNum')
        return self


class DescribeChannelUserMetricsResponseBody(TeaModel):
    def __init__(
        self,
        metric_datas: List[DescribeChannelUserMetricsResponseBodyMetricDatas] = None,
        overall_data: DescribeChannelUserMetricsResponseBodyOverallData = None,
        request_id: str = None,
    ):
        # 指标数据列表。
        self.metric_datas = metric_datas
        # 总览数据
        self.overall_data = overall_data
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.metric_datas:
            for k in self.metric_datas:
                if k:
                    k.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MetricDatas'] = []
        if self.metric_datas is not None:
            for k in self.metric_datas:
                result['MetricDatas'].append(k.to_map() if k else None)
        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_datas = []
        if m.get('MetricDatas') is not None:
            for k in m.get('MetricDatas'):
                temp_model = DescribeChannelUserMetricsResponseBodyMetricDatas()
                self.metric_datas.append(temp_model.from_map(k))
        if m.get('OverallData') is not None:
            temp_model = DescribeChannelUserMetricsResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m['OverallData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChannelUserMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChannelUserMetricsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeChannelUserMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndPointEventListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        user_id_list: str = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID
        self.channel_id = channel_id
        # 创建频道时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 释放频道时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts
        # 用户ID列表，多个用英文逗号（,）分隔。
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList(TeaModel):
    def __init__(
        self,
        event_name: str = None,
        event_type: str = None,
        ts: int = None,
    ):
        # 事件名称。
        self.event_name = event_name
        # 事件类型，取值：USER：用户事件。SYSTEM：系统事件。
        self.event_type = event_type
        # 事件发生的时间，使用UNIX时间戳表示，单位：秒。
        self.ts = ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.ts is not None:
            result['Ts'] = self.ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        return self


class DescribeEndPointEventListResponseBodyNodesEventDataItems(TeaModel):
    def __init__(
        self,
        event_list: List[DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList] = None,
        ts: int = None,
    ):
        # 事件列表。
        self.event_list = event_list
        # 第一个事件发生的时间，使用UNIX时间戳表示，单位：秒。
        self.ts = ts

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.ts is not None:
            result['Ts'] = self.ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        return self


class DescribeEndPointEventListResponseBodyNodes(TeaModel):
    def __init__(
        self,
        event_data_items: List[DescribeEndPointEventListResponseBodyNodesEventDataItems] = None,
        user_id: str = None,
    ):
        # 事件数据列表
        self.event_data_items = event_data_items
        # 用户ID
        self.user_id = user_id

    def validate(self):
        if self.event_data_items:
            for k in self.event_data_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventDataItems'] = []
        if self.event_data_items is not None:
            for k in self.event_data_items:
                result['EventDataItems'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_data_items = []
        if m.get('EventDataItems') is not None:
            for k in m.get('EventDataItems'):
                temp_model = DescribeEndPointEventListResponseBodyNodesEventDataItems()
                self.event_data_items.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEndPointEventListResponseBody(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeEndPointEventListResponseBodyNodes] = None,
        request_id: str = None,
    ):
        # 用户基本信息列表。
        self.nodes = nodes
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeEndPointEventListResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEndPointEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEndPointEventListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEndPointEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndPointMetricDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        metrics: str = None,
        pub_call_id_list: str = None,
        pub_user_id: str = None,
        sub_user_id: str = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID
        self.channel_id = channel_id
        # 创建频道时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 释放频道时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts
        # 指标枚举列表，以半角逗号分隔，包括以下类型APP_CPU APPCPU SYSTEM_CPU 系统CPU APP_MEMORY APP内存 SYSTEM_MEMORY 系统占用内存 SYSTEM_TOTAL_MEMORY 系统总内存 AUDIO_LOST_RATE 音频丢包率 VIDEO_LOST_RATE 视频丢包率 AUDIO_RTT 音频延时 VIDEO_RTT 视频延时 AUDIO_END_TO_END_RTT 音频端到端延时 VIDEO_END_TO_END_RTT 视频端到端延时 AUDIO_BIT_RATE 音频码率 AUDIO_STUCK 音频卡顿 AUDIO_LEVEL 音量 VIDEO_BIT_RATE_CAMERA 视频码率 VIDEO_BIT_RATE_LARGE 视频码率（大画面） VIDEO_BIT_RATE_SMALL 视频码率（小画面） VIDEO_BIT_RATE_SUPER 视频码率（超大屏幕） VIDEO_BIT_RATE_SHARE 视频码率（屏幕分享） VIDEO_STUCK_CAMERA 视频卡顿 VIDEO_STUCK_LARGE 视频卡顿（大画面） VIDEO_STUCK_SMALL 视频卡顿（小画面） VIDEO_STUCK_SUPER 视频卡顿（超大屏幕） VIDEO_STUCK_SHARE 视频卡顿（屏幕分享） VIDEO_RESOLUTION_CAMERA 视频分辨率 VIDEO_RESOLUTION_LARGE 视频分辨率（大画面） VIDEO_RESOLUTION_SMALL 视频分辨率（小画面） VIDEO_RESOLUTION_SUPER 视频分辨率（超大屏幕） VIDEO_RESOLUTION_SHARE 视频分辨率（屏幕分享） VIDEO_FPS_CAMERA 视频帧率 VIDEO_FPS_LARGE 视频帧率（大画面） VIDEO_FPS_SMALL 视频帧率（小画面） VIDEO_FPS_SUPER 视频帧率（超大屏幕） VIDEO_FPS_SHARE 视频帧率（屏幕分享）
        self.metrics = metrics
        # 发布端用户通信流的Call ID，多个用英文逗号（,）分隔。
        self.pub_call_id_list = pub_call_id_list
        # 发布端用户ID。
        self.pub_user_id = pub_user_id
        # 订阅端用户ID。
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.pub_call_id_list is not None:
            result['PubCallIdList'] = self.pub_call_id_list
        if self.pub_user_id is not None:
            result['PubUserId'] = self.pub_user_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('PubCallIdList') is not None:
            self.pub_call_id_list = m.get('PubCallIdList')
        if m.get('PubUserId') is not None:
            self.pub_user_id = m.get('PubUserId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribeEndPointMetricDataResponseBodyPubMetricsNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        # 拓展属性
        self.ext = ext
        # 发布端指标趋势图中x轴横坐标。
        self.x = x
        # 发布端指标趋势图中y轴纵坐标。
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeEndPointMetricDataResponseBodyPubMetrics(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeEndPointMetricDataResponseBodyPubMetricsNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        # 坐标点列表
        self.nodes = nodes
        # 对应入参Metrics中的类型
        self.type = type
        # 用户ID。
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeEndPointMetricDataResponseBodyPubMetricsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEndPointMetricDataResponseBodySubMetricsNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        # 拓展属性
        self.ext = ext
        # 订阅端指标趋势图中x轴横坐标。
        self.x = x
        # 订阅端指标趋势图y轴纵坐标。
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeEndPointMetricDataResponseBodySubMetrics(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeEndPointMetricDataResponseBodySubMetricsNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        # 订阅端指标趋势图坐标点列表。
        self.nodes = nodes
        # 对应入参Metrics中的类型
        self.type = type
        # 用户ID。
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeEndPointMetricDataResponseBodySubMetricsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeEndPointMetricDataResponseBody(TeaModel):
    def __init__(
        self,
        pub_metrics: List[DescribeEndPointMetricDataResponseBodyPubMetrics] = None,
        request_id: str = None,
        sub_metrics: List[DescribeEndPointMetricDataResponseBodySubMetrics] = None,
    ):
        # 发布端用户指标数据。
        self.pub_metrics = pub_metrics
        # 请求ID。
        self.request_id = request_id
        # 订阅端用户指标数据。
        self.sub_metrics = sub_metrics

    def validate(self):
        if self.pub_metrics:
            for k in self.pub_metrics:
                if k:
                    k.validate()
        if self.sub_metrics:
            for k in self.sub_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PubMetrics'] = []
        if self.pub_metrics is not None:
            for k in self.pub_metrics:
                result['PubMetrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubMetrics'] = []
        if self.sub_metrics is not None:
            for k in self.sub_metrics:
                result['SubMetrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pub_metrics = []
        if m.get('PubMetrics') is not None:
            for k in m.get('PubMetrics'):
                temp_model = DescribeEndPointMetricDataResponseBodyPubMetrics()
                self.pub_metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sub_metrics = []
        if m.get('SubMetrics') is not None:
            for k in m.get('SubMetrics'):
                temp_model = DescribeEndPointMetricDataResponseBodySubMetrics()
                self.sub_metrics.append(temp_model.from_map(k))
        return self


class DescribeEndPointMetricDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEndPointMetricDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEndPointMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisFactorDistributionStatRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        start_ts: int = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 查询的结束时间，使用UNIX时间戳表示，单位：秒。
        self.end_ts = end_ts
        # 查询的开始时间，使用UNIX时间戳表示，单位：秒。
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        return self


class DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList(TeaModel):
    def __init__(
        self,
        factor_id: str = None,
        user_count: int = None,
        user_ratio: float = None,
    ):
        # 影响因素ID： 1：发布端网络差 2：订阅端网络差 3：发布端设备性能差 4：发布端关闭摄像头 5：发布端切到后台运行，UNKNOWN：未知
        self.factor_id = factor_id
        # 影响用户数
        self.user_count = user_count
        # 影响用户占比
        self.user_ratio = user_ratio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factor_id is not None:
            result['FactorId'] = self.factor_id
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.user_ratio is not None:
            result['UserRatio'] = self.user_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FactorId') is not None:
            self.factor_id = m.get('FactorId')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('UserRatio') is not None:
            self.user_ratio = m.get('UserRatio')
        return self


class DescribeFaultDiagnosisFactorDistributionStatResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stat_list: List[DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList] = None,
    ):
        # 请求ID。
        self.request_id = request_id
        # 影响因素分布统计数据
        self.stat_list = stat_list

    def validate(self):
        if self.stat_list:
            for k in self.stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatList'] = []
        if self.stat_list is not None:
            for k in self.stat_list:
                result['StatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stat_list = []
        if m.get('StatList') is not None:
            for k in m.get('StatList'):
                temp_model = DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisFactorDistributionStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFaultDiagnosisFactorDistributionStatResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFaultDiagnosisFactorDistributionStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisOverallDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        start_ts: int = None,
        stat_dim: str = None,
    ):
        # APP ID
        self.app_id = app_id
        # 结束时间，秒级时间戳：1609344000
        self.end_ts = end_ts
        # 开始时间，秒级时间戳：1609344000
        self.start_ts = start_ts
        # 获取数据统计维度： JOIN_SLOW_USER：进频道慢用户数 AUDIO_STUCK_USER：音频卡顿用户数 VIDEO_STUCK_USER：视频卡顿用户数 VIDEO_VAGUE_USER：视频模糊用户数 HIGH_DELAY_USER：通话延迟高用户数 FIRST_SCREEN_SLOW_USER：接收首屏慢用户数
        self.stat_dim = stat_dim

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        # 拓展属性，ratio：单位时间内异常用户占比，totalCount：单位时间内用户总数
        self.ext = ext
        # x轴横坐标，秒级时间戳
        self.x = x
        # y轴横坐标，单位数据异常用户数
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeFaultDiagnosisOverallDataResponseBodyMetricData(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes] = None,
    ):
        # 指标坐标点列表，单位时间为1分钟的异常用户数据
        self.nodes = nodes

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisOverallDataResponseBodyOverallData(TeaModel):
    def __init__(
        self,
        fault_user_count: int = None,
        fault_user_ratio: float = None,
        total_user_count: int = None,
    ):
        # 异常用户数/人次
        self.fault_user_count = fault_user_count
        # 异常用户总占比
        self.fault_user_ratio = fault_user_ratio
        # 用户总数/人次
        self.total_user_count = total_user_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fault_user_count is not None:
            result['FaultUserCount'] = self.fault_user_count
        if self.fault_user_ratio is not None:
            result['FaultUserRatio'] = self.fault_user_ratio
        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultUserCount') is not None:
            self.fault_user_count = m.get('FaultUserCount')
        if m.get('FaultUserRatio') is not None:
            self.fault_user_ratio = m.get('FaultUserRatio')
        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')
        return self


class DescribeFaultDiagnosisOverallDataResponseBody(TeaModel):
    def __init__(
        self,
        metric_data: DescribeFaultDiagnosisOverallDataResponseBodyMetricData = None,
        overall_data: DescribeFaultDiagnosisOverallDataResponseBodyOverallData = None,
        request_id: str = None,
    ):
        # 异常指标数据
        self.metric_data = metric_data
        # 总览数据
        self.overall_data = overall_data
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.metric_data:
            self.metric_data.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_data is not None:
            result['MetricData'] = self.metric_data.to_map()
        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricData') is not None:
            temp_model = DescribeFaultDiagnosisOverallDataResponseBodyMetricData()
            self.metric_data = temp_model.from_map(m['MetricData'])
        if m.get('OverallData') is not None:
            temp_model = DescribeFaultDiagnosisOverallDataResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m['OverallData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFaultDiagnosisOverallDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFaultDiagnosisOverallDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFaultDiagnosisOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisUserDetailRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        fault_type: str = None,
        query_call_user_info: bool = None,
        user_id: str = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID
        self.channel_id = channel_id
        # 频道创建时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 异常类型 JOIN_SLOW：进频道慢 AUDIO_STUCK：音频卡顿 VIDEO_STUCK：视频卡顿 VIDEO_VAGUE：视频模糊 HIGH_DELAY：通话延迟高 FIRST_FRAME_SLOW：接收首屏慢
        self.fault_type = fault_type
        # 是否查询通话用户信息，为空默认是false
        self.query_call_user_info = query_call_user_info
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.fault_type is not None:
            result['FaultType'] = self.fault_type
        if self.query_call_user_info is not None:
            result['QueryCallUserInfo'] = self.query_call_user_info
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')
        if m.get('QueryCallUserInfo') is not None:
            self.query_call_user_info = m.get('QueryCallUserInfo')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyCallInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
    ):
        # App ID。
        self.app_id = app_id
        # 通信状态。取值：IN：进行中。OUT：已结束。
        self.call_status = call_status
        # 频道ID。
        self.channel_id = channel_id
        # 创建通信时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 释放通信时间，使用UNIX时间戳表示，单位：秒。
        self.destroyed_ts = destroyed_ts
        # 通信持续时长，单位：秒。
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList(TeaModel):
    def __init__(
        self,
        event_name: str = None,
        event_type: str = None,
        ts: int = None,
    ):
        # 事件名称。
        self.event_name = event_name
        # 事件类型，取值：USER：用户事件。SYSTEM：系统事件。
        self.event_type = event_type
        # 事件发生的时间，使用UNIX时间戳表示，单位：秒。
        self.ts = ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.ts is not None:
            result['Ts'] = self.ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems(TeaModel):
    def __init__(
        self,
        event_list: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList] = None,
        ts: int = None,
    ):
        # 事件列表。
        self.event_list = event_list
        # 第一个事件发生的时间，使用UNIX时间戳表示，单位：秒。
        self.ts = ts

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.ts is not None:
            result['Ts'] = self.ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas(TeaModel):
    def __init__(
        self,
        event_data_items: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems] = None,
        role: str = None,
        user_id: str = None,
    ):
        # 事件数据列表
        self.event_data_items = event_data_items
        # 来源角色： SENDER：发布端，即上行 RECEIVER：订阅端，即下行
        self.role = role
        # 用户ID
        self.user_id = user_id

    def validate(self):
        if self.event_data_items:
            for k in self.event_data_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventDataItems'] = []
        if self.event_data_items is not None:
            for k in self.event_data_items:
                result['EventDataItems'].append(k.to_map() if k else None)
        if self.role is not None:
            result['Role'] = self.role
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_data_items = []
        if m.get('EventDataItems') is not None:
            for k in m.get('EventDataItems'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems()
                self.event_data_items.append(temp_model.from_map(k))
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes(TeaModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        # 扩展数据
        self.ext = ext
        # X坐标值，秒级时间戳
        self.x = x
        # Y坐标值，指标值
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes] = None,
        role: str = None,
        type: str = None,
        user_id: str = None,
    ):
        # 坐标数据列表
        self.nodes = nodes
        # 来源角色： SENDER：发布端，即上行 RECEIVER：订阅端，即下行
        self.role = role
        # 指标类型，参照端到端指标接口的指标类型
        self.type = type
        # 数据来自对应发布端的用户ID
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.role is not None:
            result['Role'] = self.role
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFactorList(TeaModel):
    def __init__(
        self,
        factor_id: str = None,
        fault_source: str = None,
        related_event_datas: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas] = None,
        related_metric_datas: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas] = None,
    ):
        # 影响因素ID： 1：发布端网络差 2：订阅端网络差 3：发布端设备性能差 4：发布端关闭摄像头 5：发布端切到后台运行
        self.factor_id = factor_id
        # 异常来源 LOCAL：本端 REMOTE：远端
        self.fault_source = fault_source
        # 关联的事件，按时间分组，当FaultType为AUDIO_STUCK、VIDEO_STUCK、VIDEO_VAGUE、HIGH_DELAY时返回
        self.related_event_datas = related_event_datas
        # 关联的指标，坐标数据，当FaultType为AUDIO_STUCK、VIDEO_STUCK、VIDEO_VAGUE、HIGH_DELAY时返回
        self.related_metric_datas = related_metric_datas

    def validate(self):
        if self.related_event_datas:
            for k in self.related_event_datas:
                if k:
                    k.validate()
        if self.related_metric_datas:
            for k in self.related_metric_datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factor_id is not None:
            result['FactorId'] = self.factor_id
        if self.fault_source is not None:
            result['FaultSource'] = self.fault_source
        result['RelatedEventDatas'] = []
        if self.related_event_datas is not None:
            for k in self.related_event_datas:
                result['RelatedEventDatas'].append(k.to_map() if k else None)
        result['RelatedMetricDatas'] = []
        if self.related_metric_datas is not None:
            for k in self.related_metric_datas:
                result['RelatedMetricDatas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FactorId') is not None:
            self.factor_id = m.get('FactorId')
        if m.get('FaultSource') is not None:
            self.fault_source = m.get('FaultSource')
        self.related_event_datas = []
        if m.get('RelatedEventDatas') is not None:
            for k in m.get('RelatedEventDatas'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas()
                self.related_event_datas.append(temp_model.from_map(k))
        self.related_metric_datas = []
        if m.get('RelatedMetricDatas') is not None:
            for k in m.get('RelatedMetricDatas'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas()
                self.related_metric_datas.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes(TeaModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        # x轴坐标值，秒级时间戳，单位时间为分钟
        self.x = x
        # y轴坐标值，异常指标的值
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes] = None,
    ):
        # 指标坐标点列表
        self.nodes = nodes

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        # 加入通话时间，使用UNIX时间戳表示，单位：秒。
        self.join_ts = join_ts
        # 离开通话时间，使用UNIX时间戳表示，单位：秒。
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribeFaultDiagnosisUserDetailResponseBodyUserDetail(TeaModel):
    def __init__(
        self,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        location: str = None,
        network: str = None,
        online_duration: int = None,
        online_periods: List[DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods] = None,
        os: str = None,
        sdk_version: str = None,
        user_id: str = None,
    ):
        # 创建通话时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 释放通话时间，使用UNIX时间戳表示，单位：秒。通话未结束时值为0。
        self.destroyed_ts = destroyed_ts
        # 通话时长，首次进入到最后离开，单位：秒。
        self.duration = duration
        # 地理位置信息，例如：北京市-北京市
        self.location = location
        # 网络类型，如WiFi，4G等
        self.network = network
        # 在线时长，单位：秒。
        self.online_duration = online_duration
        # 在线时段信息。
        self.online_periods = online_periods
        # 平台类型：若用户客户端为WEB则是浏览器类型，若客户端为NATIVE则是操作系统类型
        self.os = os
        # SDK版本，如1.0.0、1.1.1等
        self.sdk_version = sdk_version
        # 用户ID。
        self.user_id = user_id

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserDetailResponseBody(TeaModel):
    def __init__(
        self,
        call_info: DescribeFaultDiagnosisUserDetailResponseBodyCallInfo = None,
        factor_list: List[DescribeFaultDiagnosisUserDetailResponseBodyFactorList] = None,
        fault_metric_data: DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData = None,
        network_operators: List[str] = None,
        request_id: str = None,
        user_detail: DescribeFaultDiagnosisUserDetailResponseBodyUserDetail = None,
    ):
        # 通信基本信息，QueryCallUserInfo=false是返回。
        self.call_info = call_info
        # 影响因素列表，空表示影响因素未知
        self.factor_list = factor_list
        # 异常指标
        self.fault_metric_data = fault_metric_data
        # 网络运营商列表
        self.network_operators = network_operators
        # 请求ID。
        self.request_id = request_id
        # 诊断用户详细信，QueryCallUserInfo=false是返回息
        self.user_detail = user_detail

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.factor_list:
            for k in self.factor_list:
                if k:
                    k.validate()
        if self.fault_metric_data:
            self.fault_metric_data.validate()
        if self.user_detail:
            self.user_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()
        result['FactorList'] = []
        if self.factor_list is not None:
            for k in self.factor_list:
                result['FactorList'].append(k.to_map() if k else None)
        if self.fault_metric_data is not None:
            result['FaultMetricData'] = self.fault_metric_data.to_map()
        if self.network_operators is not None:
            result['NetworkOperators'] = self.network_operators
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_detail is not None:
            result['UserDetail'] = self.user_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = DescribeFaultDiagnosisUserDetailResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m['CallInfo'])
        self.factor_list = []
        if m.get('FactorList') is not None:
            for k in m.get('FactorList'):
                temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFactorList()
                self.factor_list.append(temp_model.from_map(k))
        if m.get('FaultMetricData') is not None:
            temp_model = DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData()
            self.fault_metric_data = temp_model.from_map(m['FaultMetricData'])
        if m.get('NetworkOperators') is not None:
            self.network_operators = m.get('NetworkOperators')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserDetail') is not None:
            temp_model = DescribeFaultDiagnosisUserDetailResponseBodyUserDetail()
            self.user_detail = temp_model.from_map(m['UserDetail'])
        return self


class DescribeFaultDiagnosisUserDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFaultDiagnosisUserDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFaultDiagnosisUserDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaultDiagnosisUserListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        end_ts: int = None,
        fault_types: str = None,
        page_no: int = None,
        page_size: int = None,
        start_ts: int = None,
        user_id: str = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 搜索的频道ID
        self.channel_id = channel_id
        # 查询的结束时间，使用UNIX时间戳表示，单位：秒。
        self.end_ts = end_ts
        # 过滤的异常类型，多个使用半角逗号分隔 JOIN_SLOW：进频道慢 AUDIO_STUCK：音频卡顿 VIDEO_STUCK：视频卡顿 VIDEO_VAGUE：视频模糊 HIGH_DELAY：通话延迟高 FIRST_FRAME_SLOW：接收首屏慢
        self.fault_types = fault_types
        # 页码
        self.page_no = page_no
        # 每页数量
        self.page_size = page_size
        # 查询的开始时间，使用UNIX时间戳表示，单位：秒。
        self.start_ts = start_ts
        # 搜索的用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.fault_types is not None:
            result['FaultTypes'] = self.fault_types
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('FaultTypes') is not None:
            self.fault_types = m.get('FaultTypes')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserListResponseBodyUserListFaultList(TeaModel):
    def __init__(
        self,
        fault_type: str = None,
    ):
        # 异常类型 JOIN_SLOW：进频道慢 AUDIO_STUCK：音频卡顿 VIDEO_STUCK：视频卡顿 VIDEO_VAGUE：视频模糊 HIGH_DELAY：通话延迟高 FIRST_FRAME_SLOW：接收首屏慢
        self.fault_type = fault_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fault_type is not None:
            result['FaultType'] = self.fault_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')
        return self


class DescribeFaultDiagnosisUserListResponseBodyUserList(TeaModel):
    def __init__(
        self,
        channel_created_ts: int = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        fault_list: List[DescribeFaultDiagnosisUserListResponseBodyUserListFaultList] = None,
        user_id: str = None,
    ):
        # 通信的创建时间戳，使用UNIX时间戳表示，单位：秒。
        self.channel_created_ts = channel_created_ts
        # 频道ID。
        self.channel_id = channel_id
        # 用户首次进入通话时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 用户最后一次离开通话时间，使用UNIX时间戳表示，单位：秒。
        self.destroyed_ts = destroyed_ts
        # 异常列表。
        self.fault_list = fault_list
        # 用户ID。
        self.user_id = user_id

    def validate(self):
        if self.fault_list:
            for k in self.fault_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_created_ts is not None:
            result['ChannelCreatedTs'] = self.channel_created_ts
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        result['FaultList'] = []
        if self.fault_list is not None:
            for k in self.fault_list:
                result['FaultList'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCreatedTs') is not None:
            self.channel_created_ts = m.get('ChannelCreatedTs')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        self.fault_list = []
        if m.get('FaultList') is not None:
            for k in m.get('FaultList'):
                temp_model = DescribeFaultDiagnosisUserListResponseBodyUserListFaultList()
                self.fault_list.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFaultDiagnosisUserListResponseBody(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
        user_list: List[DescribeFaultDiagnosisUserListResponseBodyUserList] = None,
    ):
        # 页码。
        self.page_no = page_no
        # 每页数量。
        self.page_size = page_size
        # 请求ID。
        self.request_id = request_id
        # 总数量。
        self.total_cnt = total_cnt
        # 异常用户明细列表。
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        self.user_list = []
        if m.get('UserList') is not None:
            for k in m.get('UserList'):
                temp_model = DescribeFaultDiagnosisUserListResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class DescribeFaultDiagnosisUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFaultDiagnosisUserListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFaultDiagnosisUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIceDurPeriodByDaySubTypeRequest(TeaModel):
    def __init__(
        self,
        end_ts: int = None,
        job_type: str = None,
        start_ts: int = None,
        time_zone: str = None,
    ):
        # 结束是时间戳
        self.end_ts = end_ts
        # 任务类型
        self.job_type = job_type
        # 起始时间戳
        self.start_ts = start_ts
        # 时区
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoListSubJobInfoList(TeaModel):
    def __init__(
        self,
        sub_job_duration: int = None,
        sub_job_type: str = None,
    ):
        # 子任务时长
        self.sub_job_duration = sub_job_duration
        # 子任务类型
        self.sub_job_type = sub_job_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_job_duration is not None:
            result['SubJobDuration'] = self.sub_job_duration
        if self.sub_job_type is not None:
            result['SubJobType'] = self.sub_job_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubJobDuration') is not None:
            self.sub_job_duration = m.get('SubJobDuration')
        if m.get('SubJobType') is not None:
            self.sub_job_type = m.get('SubJobType')
        return self


class DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoList(TeaModel):
    def __init__(
        self,
        date_ts: int = None,
        duration: int = None,
        sub_job_info_list: List[DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoListSubJobInfoList] = None,
    ):
        # 日期时间戳
        self.date_ts = date_ts
        # 任务总时长,单位分钟
        self.duration = duration
        # 子任务信息列表
        self.sub_job_info_list = sub_job_info_list

    def validate(self):
        if self.sub_job_info_list:
            for k in self.sub_job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_ts is not None:
            result['DateTs'] = self.date_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        result['SubJobInfoList'] = []
        if self.sub_job_info_list is not None:
            for k in self.sub_job_info_list:
                result['SubJobInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateTs') is not None:
            self.date_ts = m.get('DateTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.sub_job_info_list = []
        if m.get('SubJobInfoList') is not None:
            for k in m.get('SubJobInfoList'):
                temp_model = DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoListSubJobInfoList()
                self.sub_job_info_list.append(temp_model.from_map(k))
        return self


class DescribeIceDurPeriodByDaySubTypeResponseBody(TeaModel):
    def __init__(
        self,
        job_info_list: List[DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoList] = None,
        request_id: str = None,
    ):
        # 任务信息列表
        self.job_info_list = job_info_list
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.job_info_list:
            for k in self.job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobInfoList'] = []
        if self.job_info_list is not None:
            for k in self.job_info_list:
                result['JobInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_info_list = []
        if m.get('JobInfoList') is not None:
            for k in m.get('JobInfoList'):
                temp_model = DescribeIceDurPeriodByDaySubTypeResponseBodyJobInfoList()
                self.job_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIceDurPeriodByDaySubTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIceDurPeriodByDaySubTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIceDurPeriodByDaySubTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIceDurSummaryOverviewRequest(TeaModel):
    def __init__(
        self,
        cur_ts: int = None,
        time_zone: str = None,
    ):
        # 当前时间戳
        self.cur_ts = cur_ts
        # 时区
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_ts is not None:
            result['CurTs'] = self.cur_ts
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurTs') is not None:
            self.cur_ts = m.get('CurTs')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class DescribeIceDurSummaryOverviewResponseBodyJobInfoList(TeaModel):
    def __init__(
        self,
        duration: int = None,
        job_type: str = None,
        time_range: str = None,
    ):
        # 任务时长
        self.duration = duration
        # 作业类型
        self.job_type = job_type
        # 时间维度
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        return self


class DescribeIceDurSummaryOverviewResponseBody(TeaModel):
    def __init__(
        self,
        job_info_list: List[DescribeIceDurSummaryOverviewResponseBodyJobInfoList] = None,
        request_id: str = None,
    ):
        # 任务信息
        self.job_info_list = job_info_list
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.job_info_list:
            for k in self.job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobInfoList'] = []
        if self.job_info_list is not None:
            for k in self.job_info_list:
                result['JobInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_info_list = []
        if m.get('JobInfoList') is not None:
            for k in m.get('JobInfoList'):
                temp_model = DescribeIceDurSummaryOverviewResponseBodyJobInfoList()
                self.job_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIceDurSummaryOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIceDurSummaryOverviewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIceDurSummaryOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePubUserListBySubUserRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        sub_user_id: str = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID。
        self.channel_id = channel_id
        # 频道创建时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 频道释放时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts
        # 订阅端用户ID。
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        # 加入通话时间，使用UNIX时间戳表示，单位：秒。
        self.join_ts = join_ts
        # 离开通话时间，使用UNIX时间戳表示，单位：秒。
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribePubUserListBySubUserResponseBodyPubUserDetailList(TeaModel):
    def __init__(
        self,
        call_id_list: List[str] = None,
        client_type: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        location: str = None,
        network: str = None,
        network_list: List[str] = None,
        online_duration: int = None,
        online_periods: List[DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods] = None,
        os: str = None,
        os_list: List[str] = None,
        roles: List[str] = None,
        sdk_version: str = None,
        sdk_version_list: List[str] = None,
        user_id: str = None,
        user_id_alias: str = None,
    ):
        # 用户通信流的Call ID。
        self.call_id_list = call_id_list
        # 端类型，取值：WEB：Web端。NATIVE：本地端。
        self.client_type = client_type
        # 第一次加入通话的时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 最后一次离开通话的时间，使用UNIX时间戳表示，单位：秒。
        self.destroyed_ts = destroyed_ts
        # 通话时长，首次进入到最后离开，单位：秒。
        self.duration = duration
        # 地理位置信息，例如：浙江省-杭州市。
        self.location = location
        # 网络类型，如WiFi，4G等
        self.network = network
        # 网络类型，如WiFi，4G等
        self.network_list = network_list
        # 在线时长，单位：秒。
        self.online_duration = online_duration
        # 在线时段信息。
        self.online_periods = online_periods
        # 平台类型：若用户客户端为WEB则是浏览器类型，若客户端为NATIVE则是操作系统类型
        self.os = os
        # 平台类型：若用户客户端为WEB则是浏览器类型，若客户端为NATIVE则是操作系统类型
        self.os_list = os_list
        # 用户角色，取值：SENDER：发起者。RECEIVER：接收者。
        self.roles = roles
        # SDK版本。
        self.sdk_version = sdk_version
        # SDK版本列表，如1.0.0、1.1.1等
        self.sdk_version_list = sdk_version_list
        # 用户ID。
        self.user_id = user_id
        # 用户ID别称
        self.user_id_alias = user_id_alias

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id_list is not None:
            result['CallIdList'] = self.call_id_list
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.network_list is not None:
            result['NetworkList'] = self.network_list
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.os_list is not None:
            result['OsList'] = self.os_list
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sdk_version_list is not None:
            result['SdkVersionList'] = self.sdk_version_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_id_alias is not None:
            result['UserIdAlias'] = self.user_id_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallIdList') is not None:
            self.call_id_list = m.get('CallIdList')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NetworkList') is not None:
            self.network_list = m.get('NetworkList')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribePubUserListBySubUserResponseBodyPubUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsList') is not None:
            self.os_list = m.get('OsList')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('SdkVersionList') is not None:
            self.sdk_version_list = m.get('SdkVersionList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')
        return self


class DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods(TeaModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        # 加入通话时间，使用UNIX时间戳表示，单位：秒。
        self.join_ts = join_ts
        # 离开通话时间，使用UNIX时间戳表示，单位：秒。
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts
        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')
        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')
        return self


class DescribePubUserListBySubUserResponseBodySubUserDetail(TeaModel):
    def __init__(
        self,
        client_type: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        location: str = None,
        network: str = None,
        network_list: List[str] = None,
        online_duration: int = None,
        online_periods: List[DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods] = None,
        os: str = None,
        os_list: List[str] = None,
        roles: List[str] = None,
        sdk_version: str = None,
        sdk_version_list: List[str] = None,
        user_id: str = None,
        user_id_alias: str = None,
    ):
        # 端类型，取值：WEB：Web端。NATIVE：本地端。
        self.client_type = client_type
        # 第一次加入通话的时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 最后一次离开通话的时间，使用UNIX时间戳表示，单位：秒。通话未结束时值为0。
        self.destroyed_ts = destroyed_ts
        # 通话时长，首次进入到最后离开，单位：秒。
        self.duration = duration
        # 地理位置信息，例如：浙江省-杭州市。
        self.location = location
        # 网络类型，如WiFi，4G等
        self.network = network
        # 网络类型，如WiFi，4G等
        self.network_list = network_list
        # 在线时长，单位：秒。
        self.online_duration = online_duration
        # 在线时段信息。
        self.online_periods = online_periods
        # 平台类型：若用户客户端为WEB则是浏览器类型，若客户端为NATIVE则是操作系统类型
        self.os = os
        # 平台类型：若用户客户端为WEB则是浏览器类型，若客户端为NATIVE则是操作系统类型
        self.os_list = os_list
        # 用户角色，取值：SENDER：发布端。RECEIVER：订阅端。
        self.roles = roles
        # SDK版本。
        self.sdk_version = sdk_version
        # SDK版本列表，如1.0.0、1.1.1等
        self.sdk_version_list = sdk_version_list
        # 用户ID。
        self.user_id = user_id
        # 用户ID别称
        self.user_id_alias = user_id_alias

    def validate(self):
        if self.online_periods:
            for k in self.online_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.location is not None:
            result['Location'] = self.location
        if self.network is not None:
            result['Network'] = self.network
        if self.network_list is not None:
            result['NetworkList'] = self.network_list
        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration
        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k in self.online_periods:
                result['OnlinePeriods'].append(k.to_map() if k else None)
        if self.os is not None:
            result['Os'] = self.os
        if self.os_list is not None:
            result['OsList'] = self.os_list
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sdk_version_list is not None:
            result['SdkVersionList'] = self.sdk_version_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_id_alias is not None:
            result['UserIdAlias'] = self.user_id_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NetworkList') is not None:
            self.network_list = m.get('NetworkList')
        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')
        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k in m.get('OnlinePeriods'):
                temp_model = DescribePubUserListBySubUserResponseBodySubUserDetailOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k))
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsList') is not None:
            self.os_list = m.get('OsList')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('SdkVersionList') is not None:
            self.sdk_version_list = m.get('SdkVersionList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserIdAlias') is not None:
            self.user_id_alias = m.get('UserIdAlias')
        return self


class DescribePubUserListBySubUserResponseBody(TeaModel):
    def __init__(
        self,
        call_status: str = None,
        pub_user_detail_list: List[DescribePubUserListBySubUserResponseBodyPubUserDetailList] = None,
        request_id: str = None,
        sub_user_detail: DescribePubUserListBySubUserResponseBodySubUserDetail = None,
    ):
        # 通信状态。取值：IN：进行中。OUT：已结束。
        self.call_status = call_status
        # 发布端用户详情信息。
        self.pub_user_detail_list = pub_user_detail_list
        # 请求ID。
        self.request_id = request_id
        # 订阅端用户详细信息。
        self.sub_user_detail = sub_user_detail

    def validate(self):
        if self.pub_user_detail_list:
            for k in self.pub_user_detail_list:
                if k:
                    k.validate()
        if self.sub_user_detail:
            self.sub_user_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        result['PubUserDetailList'] = []
        if self.pub_user_detail_list is not None:
            for k in self.pub_user_detail_list:
                result['PubUserDetailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_user_detail is not None:
            result['SubUserDetail'] = self.sub_user_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        self.pub_user_detail_list = []
        if m.get('PubUserDetailList') is not None:
            for k in m.get('PubUserDetailList'):
                temp_model = DescribePubUserListBySubUserResponseBodyPubUserDetailList()
                self.pub_user_detail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubUserDetail') is not None:
            temp_model = DescribePubUserListBySubUserResponseBodySubUserDetail()
            self.sub_user_detail = temp_model.from_map(m['SubUserDetail'])
        return self


class DescribePubUserListBySubUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePubUserListBySubUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePubUserListBySubUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQoeMetricDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        user_id: str = None,
    ):
        # APP ID。
        self.app_id = app_id
        # 频道ID。
        self.channel_id = channel_id
        # 创建频道时间，使用UNIX时间戳表示，单位：秒。
        self.created_ts = created_ts
        # 频道释放时间，使用UNIX时间戳表示，单位：秒。参数为空表示获取当前时间。
        self.destroyed_ts = destroyed_ts
        # 用户ID。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts
        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')
        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeQoeMetricDataResponseBodyAudioDataNodes(TeaModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        # 音频指标趋势图中x轴横坐标。
        self.x = x
        # 音频指标趋势图中y轴纵坐标。
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeQoeMetricDataResponseBodyAudioData(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeQoeMetricDataResponseBodyAudioDataNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        # 音频指标趋势图坐标点列表。
        self.nodes = nodes
        # 通信体验，取值：AUDIO：音频码率。AUDIO_STUCK：音频下行卡顿。
        self.type = type
        # 用户ID。
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeQoeMetricDataResponseBodyAudioDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeQoeMetricDataResponseBodyVideoDataNodes(TeaModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        # 视频指标趋势图中x轴横坐标。
        self.x = x
        # 视频指标趋势图中y轴纵坐标。
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeQoeMetricDataResponseBodyVideoData(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeQoeMetricDataResponseBodyVideoDataNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        # 视频指标趋势图坐标点列表。
        self.nodes = nodes
        # 通信体验，取值：VIDEO_CAMERA：摄像头码率。VIDEO_CAMERA_LARGE：摄像头大流码率。VIDEO_CAMERA_SMALL：摄像头小流码率。VIDEO_CAMERA_SUPER：摄像头超大流码率。VIDEO_SCREEN_SHARE：共享屏幕流码率。VIDEO_STUCK_CAMERA：摄像头卡顿。VIDEO_STUCK_CAMERA_LARGE：摄像头大流卡顿。VIDEO_STUCK_CAMERA_SMALL：摄像头小流卡顿。VIDEO_STUCK_CAMERA_SUPER：摄像头超大流卡顿。VIDEO_STUCK_SCREEN_SHARE：屏幕共享卡顿。VIDEO_VAGUE_CAMERA：摄像头模糊。VIDEO_VAGUE_CAMERA_LARGE：摄像头大流模糊。VIDEO_VAGUE_CAMERA_SMALL：摄像头小流模糊。VIDEO_VAGUE_CAMERA_SUPER：摄像头超大流模糊。VIDEO_VAGUE_SCREEN_SHARE：屏幕共享模糊。
        self.type = type
        # 用户ID
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeQoeMetricDataResponseBodyVideoDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeQoeMetricDataResponseBody(TeaModel):
    def __init__(
        self,
        audio_data: List[DescribeQoeMetricDataResponseBodyAudioData] = None,
        request_id: str = None,
        video_data: List[DescribeQoeMetricDataResponseBodyVideoData] = None,
    ):
        # 音频数据。
        self.audio_data = audio_data
        # 请求ID
        self.request_id = request_id
        # 视频数据。
        self.video_data = video_data

    def validate(self):
        if self.audio_data:
            for k in self.audio_data:
                if k:
                    k.validate()
        if self.video_data:
            for k in self.video_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AudioData'] = []
        if self.audio_data is not None:
            for k in self.audio_data:
                result['AudioData'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VideoData'] = []
        if self.video_data is not None:
            for k in self.video_data:
                result['VideoData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_data = []
        if m.get('AudioData') is not None:
            for k in m.get('AudioData'):
                temp_model = DescribeQoeMetricDataResponseBodyAudioData()
                self.audio_data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.video_data = []
        if m.get('VideoData') is not None:
            for k in m.get('VideoData'):
                temp_model = DescribeQoeMetricDataResponseBodyVideoData()
                self.video_data.append(temp_model.from_map(k))
        return self


class DescribeQoeMetricDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeQoeMetricDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeQoeMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityAreaDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        parent_area: str = None,
        start_date: int = None,
    ):
        # APP ID
        self.app_id = app_id
        # 结束时间，秒级时间戳，如1609344000
        self.end_date = end_date
        # 父级地区名称，为空取世界范围（国家维度）的统计，如： ""->中国、英国 "中国"->北京市、广东省 "广东省"->广州市、深圳市、佛山市 "北京市"->北京市
        self.parent_area = parent_area
        # 开始时间，秒级时间戳，如1609344000
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.parent_area is not None:
            result['ParentArea'] = self.parent_area
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ParentArea') is not None:
            self.parent_area = m.get('ParentArea')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeQualityAreaDistributionStatDataResponseBodyQualityStatDataList(TeaModel):
    def __init__(
        self,
        audio_delay: int = None,
        audio_high_quality_transmission_rate: str = None,
        audio_speak_out_duration: int = None,
        audio_stuck_rate: str = None,
        call_duration_ratio: str = None,
        join_channel_suc_five_sec_rate: str = None,
        join_channel_suc_rate: str = None,
        name: str = None,
        video_delay: int = None,
        video_first_pic_duration: int = None,
        video_high_quality_transmission_rate: str = None,
        video_stuck_rate: str = None,
    ):
        # 音频延时，单位毫秒
        self.audio_delay = audio_delay
        # 音频优质传输率， 四位小数表示，如0.9927
        self.audio_high_quality_transmission_rate = audio_high_quality_transmission_rate
        # 音频首次出声时间，单位毫秒
        self.audio_speak_out_duration = audio_speak_out_duration
        # 音频卡顿率， 四位小数表示，如0.0034
        self.audio_stuck_rate = audio_stuck_rate
        # 通话时长用量占比，四位小数表示，如1.0000
        self.call_duration_ratio = call_duration_ratio
        # 5秒加入频道成功率， 四位小数表示，如1.0000
        self.join_channel_suc_five_sec_rate = join_channel_suc_five_sec_rate
        # 加入频道成功率， 四位小数表示，如1.0000
        self.join_channel_suc_rate = join_channel_suc_rate
        # 区域名称，如广东省
        self.name = name
        # 视频延时，单位毫秒
        self.video_delay = video_delay
        # 视频首次出图时间，单位毫秒
        self.video_first_pic_duration = video_first_pic_duration
        # 视频优质传输率，四位小数表示，如0.9965
        self.video_high_quality_transmission_rate = video_high_quality_transmission_rate
        # 视频卡顿率， 四位小数表示，如0.0038
        self.video_stuck_rate = video_stuck_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_delay is not None:
            result['AudioDelay'] = self.audio_delay
        if self.audio_high_quality_transmission_rate is not None:
            result['AudioHighQualityTransmissionRate'] = self.audio_high_quality_transmission_rate
        if self.audio_speak_out_duration is not None:
            result['AudioSpeakOutDuration'] = self.audio_speak_out_duration
        if self.audio_stuck_rate is not None:
            result['AudioStuckRate'] = self.audio_stuck_rate
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.join_channel_suc_five_sec_rate is not None:
            result['JoinChannelSucFiveSecRate'] = self.join_channel_suc_five_sec_rate
        if self.join_channel_suc_rate is not None:
            result['JoinChannelSucRate'] = self.join_channel_suc_rate
        if self.name is not None:
            result['Name'] = self.name
        if self.video_delay is not None:
            result['VideoDelay'] = self.video_delay
        if self.video_first_pic_duration is not None:
            result['VideoFirstPicDuration'] = self.video_first_pic_duration
        if self.video_high_quality_transmission_rate is not None:
            result['VideoHighQualityTransmissionRate'] = self.video_high_quality_transmission_rate
        if self.video_stuck_rate is not None:
            result['VideoStuckRate'] = self.video_stuck_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDelay') is not None:
            self.audio_delay = m.get('AudioDelay')
        if m.get('AudioHighQualityTransmissionRate') is not None:
            self.audio_high_quality_transmission_rate = m.get('AudioHighQualityTransmissionRate')
        if m.get('AudioSpeakOutDuration') is not None:
            self.audio_speak_out_duration = m.get('AudioSpeakOutDuration')
        if m.get('AudioStuckRate') is not None:
            self.audio_stuck_rate = m.get('AudioStuckRate')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('JoinChannelSucFiveSecRate') is not None:
            self.join_channel_suc_five_sec_rate = m.get('JoinChannelSucFiveSecRate')
        if m.get('JoinChannelSucRate') is not None:
            self.join_channel_suc_rate = m.get('JoinChannelSucRate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoDelay') is not None:
            self.video_delay = m.get('VideoDelay')
        if m.get('VideoFirstPicDuration') is not None:
            self.video_first_pic_duration = m.get('VideoFirstPicDuration')
        if m.get('VideoHighQualityTransmissionRate') is not None:
            self.video_high_quality_transmission_rate = m.get('VideoHighQualityTransmissionRate')
        if m.get('VideoStuckRate') is not None:
            self.video_stuck_rate = m.get('VideoStuckRate')
        return self


class DescribeQualityAreaDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        quality_stat_data_list: List[DescribeQualityAreaDistributionStatDataResponseBodyQualityStatDataList] = None,
        request_id: str = None,
    ):
        # 质量分布数据列表
        self.quality_stat_data_list = quality_stat_data_list
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.quality_stat_data_list:
            for k in self.quality_stat_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityStatDataList'] = []
        if self.quality_stat_data_list is not None:
            for k in self.quality_stat_data_list:
                result['QualityStatDataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_stat_data_list = []
        if m.get('QualityStatDataList') is not None:
            for k in m.get('QualityStatDataList'):
                temp_model = DescribeQualityAreaDistributionStatDataResponseBodyQualityStatDataList()
                self.quality_stat_data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityAreaDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeQualityAreaDistributionStatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeQualityAreaDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        stat_dim: str = None,
    ):
        # APP ID
        self.app_id = app_id
        # 结束时间，秒级时间戳，如1609344000
        self.end_date = end_date
        # 开始时间，秒级时间戳，如1609344000
        self.start_date = start_date
        # 统计维度，支持最多填入一个 CHANNEL_ONLINE, NETWORK, OS
        self.stat_dim = stat_dim

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeQualityDistributionStatDataResponseBodyQualityStatDataList(TeaModel):
    def __init__(
        self,
        audio_delay: int = None,
        audio_high_quality_transmission_rate: str = None,
        audio_speak_out_duration: int = None,
        audio_stuck_rate: str = None,
        call_duration_ratio: str = None,
        join_channel_suc_five_sec_rate: str = None,
        join_channel_suc_rate: str = None,
        name: str = None,
        video_delay: int = None,
        video_first_pic_duration: int = None,
        video_high_quality_transmission_rate: str = None,
        video_stuck_rate: str = None,
    ):
        # 音频延时，单位毫秒
        self.audio_delay = audio_delay
        # 音频优质传输率， 四位小数表示，如0.9927
        self.audio_high_quality_transmission_rate = audio_high_quality_transmission_rate
        # 音频首次出声时间，单位毫秒
        self.audio_speak_out_duration = audio_speak_out_duration
        # 音频卡顿率， 四位小数表示，如0.0034
        self.audio_stuck_rate = audio_stuck_rate
        # 通话时长用量占比，四位小数表示，如1.0000
        self.call_duration_ratio = call_duration_ratio
        # 5秒加入频道成功率， 四位小数表示，如1.0000
        self.join_channel_suc_five_sec_rate = join_channel_suc_five_sec_rate
        # 加入频道成功率， 四位小数表示，如1.0000
        self.join_channel_suc_rate = join_channel_suc_rate
        # 统计名称， 当StatDim=CHANNEL_ONLINE： ONE_TO_FIVE：1-5人 SIX_TO_TEN：6-10人 ELEVEN_TO_TWENTY：11-20人 TWENTY_ONE_TO_FIFTY: 21-50人 ABOVE_FIFTY：50人以上  当StatDim=NETWORK： WiFi，4G等  当StatDim=OS： iOS、android等
        self.name = name
        # 视频延时，单位毫秒
        self.video_delay = video_delay
        # 视频首次出图时间，单位毫秒
        self.video_first_pic_duration = video_first_pic_duration
        # 视频优质传输率，四位小数表示，如0.9965
        self.video_high_quality_transmission_rate = video_high_quality_transmission_rate
        # 视频卡顿率， 四位小数表示，如0.0038
        self.video_stuck_rate = video_stuck_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_delay is not None:
            result['AudioDelay'] = self.audio_delay
        if self.audio_high_quality_transmission_rate is not None:
            result['AudioHighQualityTransmissionRate'] = self.audio_high_quality_transmission_rate
        if self.audio_speak_out_duration is not None:
            result['AudioSpeakOutDuration'] = self.audio_speak_out_duration
        if self.audio_stuck_rate is not None:
            result['AudioStuckRate'] = self.audio_stuck_rate
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.join_channel_suc_five_sec_rate is not None:
            result['JoinChannelSucFiveSecRate'] = self.join_channel_suc_five_sec_rate
        if self.join_channel_suc_rate is not None:
            result['JoinChannelSucRate'] = self.join_channel_suc_rate
        if self.name is not None:
            result['Name'] = self.name
        if self.video_delay is not None:
            result['VideoDelay'] = self.video_delay
        if self.video_first_pic_duration is not None:
            result['VideoFirstPicDuration'] = self.video_first_pic_duration
        if self.video_high_quality_transmission_rate is not None:
            result['VideoHighQualityTransmissionRate'] = self.video_high_quality_transmission_rate
        if self.video_stuck_rate is not None:
            result['VideoStuckRate'] = self.video_stuck_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDelay') is not None:
            self.audio_delay = m.get('AudioDelay')
        if m.get('AudioHighQualityTransmissionRate') is not None:
            self.audio_high_quality_transmission_rate = m.get('AudioHighQualityTransmissionRate')
        if m.get('AudioSpeakOutDuration') is not None:
            self.audio_speak_out_duration = m.get('AudioSpeakOutDuration')
        if m.get('AudioStuckRate') is not None:
            self.audio_stuck_rate = m.get('AudioStuckRate')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('JoinChannelSucFiveSecRate') is not None:
            self.join_channel_suc_five_sec_rate = m.get('JoinChannelSucFiveSecRate')
        if m.get('JoinChannelSucRate') is not None:
            self.join_channel_suc_rate = m.get('JoinChannelSucRate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoDelay') is not None:
            self.video_delay = m.get('VideoDelay')
        if m.get('VideoFirstPicDuration') is not None:
            self.video_first_pic_duration = m.get('VideoFirstPicDuration')
        if m.get('VideoHighQualityTransmissionRate') is not None:
            self.video_high_quality_transmission_rate = m.get('VideoHighQualityTransmissionRate')
        if m.get('VideoStuckRate') is not None:
            self.video_stuck_rate = m.get('VideoStuckRate')
        return self


class DescribeQualityDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        quality_stat_data_list: List[DescribeQualityDistributionStatDataResponseBodyQualityStatDataList] = None,
        request_id: str = None,
    ):
        # 分布数据列表
        self.quality_stat_data_list = quality_stat_data_list
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.quality_stat_data_list:
            for k in self.quality_stat_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityStatDataList'] = []
        if self.quality_stat_data_list is not None:
            for k in self.quality_stat_data_list:
                result['QualityStatDataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_stat_data_list = []
        if m.get('QualityStatDataList') is not None:
            for k in m.get('QualityStatDataList'):
                temp_model = DescribeQualityDistributionStatDataResponseBodyQualityStatDataList()
                self.quality_stat_data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeQualityDistributionStatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeQualityDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityOsSdkVersionDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
    ):
        # APP ID
        self.app_id = app_id
        # 结束时间，秒级时间戳，如1609344000
        self.end_date = end_date
        # 开始时间，秒级时间戳，如1609344000
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeQualityOsSdkVersionDistributionStatDataResponseBodyQualityOsSdkVersionStatDataList(TeaModel):
    def __init__(
        self,
        audio_delay: int = None,
        audio_high_quality_transmission_rate: str = None,
        audio_speak_out_duration: int = None,
        audio_stuck_rate: str = None,
        call_duration_ratio: str = None,
        join_channel_suc_five_sec_rate: str = None,
        join_channel_suc_rate: str = None,
        name: str = None,
        os: str = None,
        video_delay: int = None,
        video_first_pic_duration: int = None,
        video_high_quality_transmission_rate: str = None,
        video_stuck_rate: str = None,
    ):
        # 音频延时，单位毫秒
        self.audio_delay = audio_delay
        # 音频优质传输率， 四位小数表示，如0.9927
        self.audio_high_quality_transmission_rate = audio_high_quality_transmission_rate
        # 音频首次出声时间，单位毫秒
        self.audio_speak_out_duration = audio_speak_out_duration
        # 音频卡顿率， 四位小数表示，如0.0034
        self.audio_stuck_rate = audio_stuck_rate
        # 通话时长用量占比，四位小数表示，如1.0000
        self.call_duration_ratio = call_duration_ratio
        # 5秒加入频道成功率， 四位小数表示，如1.0000
        self.join_channel_suc_five_sec_rate = join_channel_suc_five_sec_rate
        # 加入频道成功率， 四位小数表示，如1.0000
        self.join_channel_suc_rate = join_channel_suc_rate
        # SDK版本名称，1.0.0、1.1.1等
        self.name = name
        # 操作系统名称，iOS、android等
        self.os = os
        # 视频延时，单位毫秒
        self.video_delay = video_delay
        # 视频首次出图时间，单位毫秒
        self.video_first_pic_duration = video_first_pic_duration
        # 视频优质传输率，四位小数表示，如0.9965
        self.video_high_quality_transmission_rate = video_high_quality_transmission_rate
        # 视频卡顿率， 四位小数表示，如0.0038
        self.video_stuck_rate = video_stuck_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_delay is not None:
            result['AudioDelay'] = self.audio_delay
        if self.audio_high_quality_transmission_rate is not None:
            result['AudioHighQualityTransmissionRate'] = self.audio_high_quality_transmission_rate
        if self.audio_speak_out_duration is not None:
            result['AudioSpeakOutDuration'] = self.audio_speak_out_duration
        if self.audio_stuck_rate is not None:
            result['AudioStuckRate'] = self.audio_stuck_rate
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.join_channel_suc_five_sec_rate is not None:
            result['JoinChannelSucFiveSecRate'] = self.join_channel_suc_five_sec_rate
        if self.join_channel_suc_rate is not None:
            result['JoinChannelSucRate'] = self.join_channel_suc_rate
        if self.name is not None:
            result['Name'] = self.name
        if self.os is not None:
            result['Os'] = self.os
        if self.video_delay is not None:
            result['VideoDelay'] = self.video_delay
        if self.video_first_pic_duration is not None:
            result['VideoFirstPicDuration'] = self.video_first_pic_duration
        if self.video_high_quality_transmission_rate is not None:
            result['VideoHighQualityTransmissionRate'] = self.video_high_quality_transmission_rate
        if self.video_stuck_rate is not None:
            result['VideoStuckRate'] = self.video_stuck_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDelay') is not None:
            self.audio_delay = m.get('AudioDelay')
        if m.get('AudioHighQualityTransmissionRate') is not None:
            self.audio_high_quality_transmission_rate = m.get('AudioHighQualityTransmissionRate')
        if m.get('AudioSpeakOutDuration') is not None:
            self.audio_speak_out_duration = m.get('AudioSpeakOutDuration')
        if m.get('AudioStuckRate') is not None:
            self.audio_stuck_rate = m.get('AudioStuckRate')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('JoinChannelSucFiveSecRate') is not None:
            self.join_channel_suc_five_sec_rate = m.get('JoinChannelSucFiveSecRate')
        if m.get('JoinChannelSucRate') is not None:
            self.join_channel_suc_rate = m.get('JoinChannelSucRate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('VideoDelay') is not None:
            self.video_delay = m.get('VideoDelay')
        if m.get('VideoFirstPicDuration') is not None:
            self.video_first_pic_duration = m.get('VideoFirstPicDuration')
        if m.get('VideoHighQualityTransmissionRate') is not None:
            self.video_high_quality_transmission_rate = m.get('VideoHighQualityTransmissionRate')
        if m.get('VideoStuckRate') is not None:
            self.video_stuck_rate = m.get('VideoStuckRate')
        return self


class DescribeQualityOsSdkVersionDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        quality_os_sdk_version_stat_data_list: List[DescribeQualityOsSdkVersionDistributionStatDataResponseBodyQualityOsSdkVersionStatDataList] = None,
        request_id: str = None,
    ):
        # 分布数据列表
        self.quality_os_sdk_version_stat_data_list = quality_os_sdk_version_stat_data_list
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.quality_os_sdk_version_stat_data_list:
            for k in self.quality_os_sdk_version_stat_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityOsSdkVersionStatDataList'] = []
        if self.quality_os_sdk_version_stat_data_list is not None:
            for k in self.quality_os_sdk_version_stat_data_list:
                result['QualityOsSdkVersionStatDataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_os_sdk_version_stat_data_list = []
        if m.get('QualityOsSdkVersionStatDataList') is not None:
            for k in m.get('QualityOsSdkVersionStatDataList'):
                temp_model = DescribeQualityOsSdkVersionDistributionStatDataResponseBodyQualityOsSdkVersionStatDataList()
                self.quality_os_sdk_version_stat_data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityOsSdkVersionDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeQualityOsSdkVersionDistributionStatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeQualityOsSdkVersionDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQualityOverallDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        types: str = None,
    ):
        # APP ID
        self.app_id = app_id
        # 结束时间，秒级时间戳，如1609344000
        self.end_date = end_date
        # 开始时间，秒级时间戳，如1609344000
        self.start_date = start_date
        # 类型，以半角逗号分隔 加入频道成功率： JOIN_CHANNEL_SUC_RATE 五秒加入频道成功率： JOIN_CHANNEL_SUC_FIVE_SEC_RATE  首次出声时间： AUDIO_SPEAK_OUT_DUR 首次出图时间： VIDEO_FIRST_PIC_DUR 音频卡顿率： AUDIO_STUCK_RATE 视频卡顿率： VIDEO_STUCK_RATE 音频延时： AUDIO_DELAY 视频延时： AUDIO_DELAY 音频优质传输率： AUDIO_HIGH_QUALITY_TRANSMISSION_RATE 视频优质传输率： VIDEO_HIGH_QUALITY_TRANSMISSION_RATE
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class DescribeQualityOverallDataResponseBodyQualityOverallDataNodes(TeaModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        # x轴横坐标
        self.x = x
        # y轴纵坐标
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeQualityOverallDataResponseBodyQualityOverallData(TeaModel):
    def __init__(
        self,
        average: str = None,
        nodes: List[DescribeQualityOverallDataResponseBodyQualityOverallDataNodes] = None,
        type: str = None,
    ):
        # 平均值
        self.average = average
        # 坐标点列表
        self.nodes = nodes
        # 概览数据类型，加入频道成功率： JOIN_CHANNEL_SUC_RATE 五秒加入频道成功率： JOIN_CHANNEL_SUC_FIVE_SEC_RATE  首次出声时间： AUDIO_SPEAK_OUT_DUR 首次出图时间： VIDEO_FIRST_PIC_DUR 音频卡顿率： AUDIO_STUCK_RATE 视频卡顿率： VIDEO_STUCK_RATE 音频延时： AUDIO_DELAY 视频延时： AUDIO_DELAY 音频优质传输率： AUDIO_HIGH_QUALITY_TRANSMISSION_RATE 视频优质传输率： VIDEO_HIGH_QUALITY_TRANSMISSION_RATE
        self.type = type

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeQualityOverallDataResponseBodyQualityOverallDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeQualityOverallDataResponseBody(TeaModel):
    def __init__(
        self,
        quality_overall_data: List[DescribeQualityOverallDataResponseBodyQualityOverallData] = None,
        request_id: str = None,
    ):
        # 概览数据列表
        self.quality_overall_data = quality_overall_data
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.quality_overall_data:
            for k in self.quality_overall_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityOverallData'] = []
        if self.quality_overall_data is not None:
            for k in self.quality_overall_data:
                result['QualityOverallData'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_overall_data = []
        if m.get('QualityOverallData') is not None:
            for k in m.get('QualityOverallData'):
                temp_model = DescribeQualityOverallDataResponseBodyQualityOverallData()
                self.quality_overall_data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeQualityOverallDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeQualityOverallDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeQualityOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelDetailsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        end_time: str = None,
        page_no: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # 应用 ID
        self.app_id = app_id
        # 频道ID
        self.channel_id = channel_id
        # 结束时间，UTC时间
        self.end_time = end_time
        # 页号
        self.page_no = page_no
        # 显示数量
        self.page_size = page_size
        # 起始时间，UTC格式
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRtcChannelDetailsResponseBodyChannelInfo(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        join_time: str = None,
        leave_time: str = None,
        os: str = None,
        platform: str = None,
        sdk_version: str = None,
        sid: str = None,
        uid: str = None,
    ):
        # 设备类型
        self.device_type = device_type
        # 用户入会时间，UTC格式
        self.join_time = join_time
        # 用户离会时间，UTC格式
        self.leave_time = leave_time
        # 操作系统
        self.os = os
        # 平台信息
        self.platform = platform
        # SDK版本
        self.sdk_version = sdk_version
        # SessionID
        self.sid = sid
        # 参会者ID
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.leave_time is not None:
            result['LeaveTime'] = self.leave_time
        if self.os is not None:
            result['OS'] = self.os
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('LeaveTime') is not None:
            self.leave_time = m.get('LeaveTime')
        if m.get('OS') is not None:
            self.os = m.get('OS')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeRtcChannelDetailsResponseBody(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        channel_info: List[DescribeRtcChannelDetailsResponseBodyChannelInfo] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_size: int = None,
    ):
        # 频道ID
        self.channel_id = channel_id
        # 频道信息
        self.channel_info = channel_info
        # 页号
        self.page_no = page_no
        # 显示数量
        self.page_size = page_size
        # 请求Id
        self.request_id = request_id
        # 总数量
        self.total_size = total_size

    def validate(self):
        if self.channel_info:
            for k in self.channel_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        result['ChannelInfo'] = []
        if self.channel_info is not None:
            for k in self.channel_info:
                result['ChannelInfo'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        self.channel_info = []
        if m.get('ChannelInfo') is not None:
            for k in m.get('ChannelInfo'):
                temp_model = DescribeRtcChannelDetailsResponseBodyChannelInfo()
                self.channel_info.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeRtcChannelDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        end_time: str = None,
        page_no: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # 应用Id
        self.app_id = app_id
        # ChannelId
        self.channel_id = channel_id
        # 结束时间，UTC格式
        self.end_time = end_time
        # 页号
        self.page_no = page_no
        # 显示数量
        self.page_size = page_size
        # 起始时间，UTC格式
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRtcChannelListResponseBodyChannels(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        end_time: str = None,
        finished: bool = None,
        start_time: str = None,
    ):
        # 频道ID
        self.channel_id = channel_id
        # 频道结束时间，UTC时间
        self.end_time = end_time
        # 是否已经结束
        self.finished = finished
        # 频道开始时间，UTC格式
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRtcChannelListResponseBody(TeaModel):
    def __init__(
        self,
        channels: List[DescribeRtcChannelListResponseBodyChannels] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
    ):
        # 频道列表
        self.channels = channels
        # 页号
        self.page_no = page_no
        # 显示数量
        self.page_size = page_size
        # 请求id
        self.request_id = request_id
        # 总条数
        self.total_cnt = total_cnt

    def validate(self):
        if self.channels:
            for k in self.channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['Channels'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('Channels') is not None:
            for k in m.get('Channels'):
                temp_model = DescribeRtcChannelListResponseBodyChannels()
                self.channels.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        return self


class DescribeRtcChannelListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelMetricListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        end_time: str = None,
        pub_uid: str = None,
        start_time: str = None,
        sub_uid: str = None,
    ):
        # 应用id
        self.app_id = app_id
        # ChannelId
        self.channel_id = channel_id
        # 结束时间，UTC格式
        self.end_time = end_time
        # 发布端用户ID
        self.pub_uid = pub_uid
        # 起始时间，UTC格式
        self.start_time = start_time
        # 接收端用户ID
        self.sub_uid = sub_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pub_uid is not None:
            result['PubUid'] = self.pub_uid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PubUid') is not None:
            self.pub_uid = m.get('PubUid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        return self


class DescribeRtcChannelMetricListResponseBodyMetrics(TeaModel):
    def __init__(
        self,
        kvs: Dict[str, Any] = None,
        mid: int = None,
        uid: str = None,
    ):
        # 指标键值对,指标发生时间:指标值
        self.kvs = kvs
        # 指标ID
        self.mid = mid
        # 用户ID
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kvs is not None:
            result['KVs'] = self.kvs
        if self.mid is not None:
            result['Mid'] = self.mid
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KVs') is not None:
            self.kvs = m.get('KVs')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeRtcChannelMetricListResponseBody(TeaModel):
    def __init__(
        self,
        metrics: List[DescribeRtcChannelMetricListResponseBodyMetrics] = None,
        request_id: str = None,
    ):
        # 指标列表
        self.metrics = metrics
        # 请求Id
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = DescribeRtcChannelMetricListResponseBodyMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRtcChannelMetricListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelMetricListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelMetricListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcChannelUsersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        page_no: int = None,
        page_size: int = None,
        time_point: str = None,
    ):
        # 应用ID
        self.app_id = app_id
        # ChannelId
        self.channel_id = channel_id
        # 页号
        self.page_no = page_no
        # 显示数量
        self.page_size = page_size
        # 查询时间点日期，天粒度，UTC格式
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        return self


class DescribeRtcChannelUsersResponseBodyUserListUserList(TeaModel):
    def __init__(
        self,
        channel: str = None,
        end_time: str = None,
        location: str = None,
        pub_audio: int = None,
        pub_content: int = None,
        pub_video_1080: int = None,
        pub_video_360: int = None,
        pub_video_720: int = None,
        service_area: str = None,
        start_time: str = None,
        sub_audio: int = None,
        sub_content: int = None,
        sub_video_1080: int = None,
        sub_video_360: int = None,
        sub_video_720: int = None,
        user_id: str = None,
    ):
        # ChannelID
        self.channel = channel
        # 用户离开频道时间
        self.end_time = end_time
        # 用户地理位置
        self.location = location
        # 发布音频时长(单位分钟)
        self.pub_audio = pub_audio
        # 发布屏幕共享时长(单位分钟)
        self.pub_content = pub_content
        # 发布1080视频时长(单位分钟)
        self.pub_video_1080 = pub_video_1080
        # 发布360视频时长(单位分钟)
        self.pub_video_360 = pub_video_360
        # 发布720视频时长(单位分钟)
        self.pub_video_720 = pub_video_720
        # 服务大区
        self.service_area = service_area
        # 用户加入频道时间
        self.start_time = start_time
        # 订阅音频时长(单位分钟)
        self.sub_audio = sub_audio
        # 订阅屏幕共享时长(单位分钟)
        self.sub_content = sub_content
        # 订阅1080视频时长(单位分钟)
        self.sub_video_1080 = sub_video_1080
        # 订阅时360视频长(单位分钟)
        self.sub_video_360 = sub_video_360
        # 订阅720视频时长(单位分钟)
        self.sub_video_720 = sub_video_720
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.location is not None:
            result['Location'] = self.location
        if self.pub_audio is not None:
            result['PubAudio'] = self.pub_audio
        if self.pub_content is not None:
            result['PubContent'] = self.pub_content
        if self.pub_video_1080 is not None:
            result['PubVideo1080'] = self.pub_video_1080
        if self.pub_video_360 is not None:
            result['PubVideo360'] = self.pub_video_360
        if self.pub_video_720 is not None:
            result['PubVideo720'] = self.pub_video_720
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_audio is not None:
            result['SubAudio'] = self.sub_audio
        if self.sub_content is not None:
            result['SubContent'] = self.sub_content
        if self.sub_video_1080 is not None:
            result['SubVideo1080'] = self.sub_video_1080
        if self.sub_video_360 is not None:
            result['SubVideo360'] = self.sub_video_360
        if self.sub_video_720 is not None:
            result['SubVideo720'] = self.sub_video_720
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('PubAudio') is not None:
            self.pub_audio = m.get('PubAudio')
        if m.get('PubContent') is not None:
            self.pub_content = m.get('PubContent')
        if m.get('PubVideo1080') is not None:
            self.pub_video_1080 = m.get('PubVideo1080')
        if m.get('PubVideo360') is not None:
            self.pub_video_360 = m.get('PubVideo360')
        if m.get('PubVideo720') is not None:
            self.pub_video_720 = m.get('PubVideo720')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubAudio') is not None:
            self.sub_audio = m.get('SubAudio')
        if m.get('SubContent') is not None:
            self.sub_content = m.get('SubContent')
        if m.get('SubVideo1080') is not None:
            self.sub_video_1080 = m.get('SubVideo1080')
        if m.get('SubVideo360') is not None:
            self.sub_video_360 = m.get('SubVideo360')
        if m.get('SubVideo720') is not None:
            self.sub_video_720 = m.get('SubVideo720')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeRtcChannelUsersResponseBodyUserList(TeaModel):
    def __init__(
        self,
        user_list: List[DescribeRtcChannelUsersResponseBodyUserListUserList] = None,
    ):
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_list = []
        if m.get('UserList') is not None:
            for k in m.get('UserList'):
                temp_model = DescribeRtcChannelUsersResponseBodyUserListUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class DescribeRtcChannelUsersResponseBody(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
        user_list: DescribeRtcChannelUsersResponseBodyUserList = None,
    ):
        # 页号
        self.page_no = page_no
        # 显示数量
        self.page_size = page_size
        # 请求ID
        self.request_id = request_id
        # 总数
        self.total_cnt = total_cnt
        # 用户列表
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            self.user_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt
        if self.user_list is not None:
            result['UserList'] = self.user_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')
        if m.get('UserList') is not None:
            temp_model = DescribeRtcChannelUsersResponseBodyUserList()
            self.user_list = temp_model.from_map(m['UserList'])
        return self


class DescribeRtcChannelUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcChannelUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcChannelUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcRecordMetricDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        service_area: str = None,
        start_time: str = None,
    ):
        # appId
        self.app_id = app_id
        # 结束时间，UTC格式
        self.end_time = end_time
        # 服务区域
        self.service_area = service_area
        # 起始时间，UTC格式
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRtcRecordMetricDataResponseBodyRtcRecordMetricData(TeaModel):
    def __init__(
        self,
        duration: int = None,
        ratio: str = None,
        service_area: str = None,
        task_profile: str = None,
        time_stamp: str = None,
        type: str = None,
    ):
        # 时长分钟
        self.duration = duration
        # 分辨率
        self.ratio = ratio
        # 服务区域
        self.service_area = service_area
        # 规格
        self.task_profile = task_profile
        # 日期，UTC格式
        self.time_stamp = time_stamp
        # 输入路数
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area
        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')
        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeRtcRecordMetricDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rtc_record_metric_data: List[DescribeRtcRecordMetricDataResponseBodyRtcRecordMetricData] = None,
    ):
        # 请求Id
        self.request_id = request_id
        # 录制用量查询数据
        self.rtc_record_metric_data = rtc_record_metric_data

    def validate(self):
        if self.rtc_record_metric_data:
            for k in self.rtc_record_metric_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RtcRecordMetricData'] = []
        if self.rtc_record_metric_data is not None:
            for k in self.rtc_record_metric_data:
                result['RtcRecordMetricData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rtc_record_metric_data = []
        if m.get('RtcRecordMetricData') is not None:
            for k in m.get('RtcRecordMetricData'):
                temp_model = DescribeRtcRecordMetricDataResponseBodyRtcRecordMetricData()
                self.rtc_record_metric_data.append(temp_model.from_map(k))
        return self


class DescribeRtcRecordMetricDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcRecordMetricDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcRecordMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRtcUserEventListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        end_time: str = None,
        start_time: str = None,
        uid: str = None,
    ):
        # 应用id
        self.app_id = app_id
        # ChannelID
        self.channel_id = channel_id
        # 结束时间，UTC格式
        self.end_time = end_time
        # 起始时间，UTC格式
        self.start_time = start_time
        # 用户ID
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeRtcUserEventListResponseBodyEvents(TeaModel):
    def __init__(
        self,
        category: str = None,
        event_id: int = None,
        event_time: int = None,
    ):
        # 事件类型
        self.category = category
        # 事件Id
        self.event_id = event_id
        # 时间发生unix timestamp
        self.event_time = event_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        return self


class DescribeRtcUserEventListResponseBody(TeaModel):
    def __init__(
        self,
        events: List[DescribeRtcUserEventListResponseBodyEvents] = None,
        request_id: str = None,
    ):
        # 指标列表
        self.events = events
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeRtcUserEventListResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRtcUserEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRtcUserEventListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRtcUserEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageAreaDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: str = None,
        parent_area: str = None,
        start_date: str = None,
    ):
        # APP ID
        self.app_id = app_id
        # 结束时间，秒级时间戳，如1609344000
        self.end_date = end_date
        # 父级地区名称，为空取世界范围（国家维度）的统计，如： ""->中国、英国 "中国"->北京市、广东省 "广东省"->广州市、深圳市、佛山市 "北京市"->北京市
        self.parent_area = parent_area
        # 开始时间，秒级时间戳，如1609344000
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.parent_area is not None:
            result['ParentArea'] = self.parent_area
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ParentArea') is not None:
            self.parent_area = m.get('ParentArea')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList(TeaModel):
    def __init__(
        self,
        audio_call_duration: int = None,
        name: str = None,
        total_call_duration: int = None,
        video_call_duration: int = None,
    ):
        # 音频通话时长，单位分钟
        self.audio_call_duration = audio_call_duration
        # 地域名称，如中国
        self.name = name
        # 总通话时长，单位分钟
        self.total_call_duration = total_call_duration
        # 视频通话时长，单位分钟
        self.video_call_duration = video_call_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_call_duration is not None:
            result['AudioCallDuration'] = self.audio_call_duration
        if self.name is not None:
            result['Name'] = self.name
        if self.total_call_duration is not None:
            result['TotalCallDuration'] = self.total_call_duration
        if self.video_call_duration is not None:
            result['VideoCallDuration'] = self.video_call_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioCallDuration') is not None:
            self.audio_call_duration = m.get('AudioCallDuration')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')
        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')
        return self


class DescribeUsageAreaDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_area_stat_list: List[DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList] = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 用量统计地域分布数据
        self.usage_area_stat_list = usage_area_stat_list

    def validate(self):
        if self.usage_area_stat_list:
            for k in self.usage_area_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageAreaStatList'] = []
        if self.usage_area_stat_list is not None:
            for k in self.usage_area_stat_list:
                result['UsageAreaStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_area_stat_list = []
        if m.get('UsageAreaStatList') is not None:
            for k in m.get('UsageAreaStatList'):
                temp_model = DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList()
                self.usage_area_stat_list.append(temp_model.from_map(k))
        return self


class DescribeUsageAreaDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUsageAreaDistributionStatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUsageAreaDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        stat_dim: str = None,
    ):
        # APP ID
        self.app_id = app_id
        # 结束时间，秒级时间戳：如1609344000
        self.end_date = end_date
        # 开始时间，秒级时间戳：如1609344000
        self.start_date = start_date
        # 统计维度，支持最多填入一个 CHANNEL_ONLINE, NETWORK, OS
        self.stat_dim = stat_dim

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')
        return self


class DescribeUsageDistributionStatDataResponseBodyUsageStatList(TeaModel):
    def __init__(
        self,
        audio_call_duration: int = None,
        call_duration_ratio: str = None,
        name: str = None,
        total_call_duration: int = None,
        video_call_duration: int = None,
    ):
        # 音频通话时长，单位分钟
        self.audio_call_duration = audio_call_duration
        # 通话时长占比，四位小数表示，如1.0000
        self.call_duration_ratio = call_duration_ratio
        # 统计名称， 当StatDim=CHANNEL_ONLINE： ONE_TO_FIVE：1-5人 SIX_TO_TEN：6-10人 ELEVEN_TO_TWENTY：11-20人 TWENTY_ONE_TO_FIFTY: 21-50人 ABOVE_FIFTY：50人以上  当StatDim=NETWORK： WiFi，4G等  当StatDim=OS： iOS、android等
        self.name = name
        # 总通话时长，单位分钟
        self.total_call_duration = total_call_duration
        # 视频通话时长，单位分钟
        self.video_call_duration = video_call_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_call_duration is not None:
            result['AudioCallDuration'] = self.audio_call_duration
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.name is not None:
            result['Name'] = self.name
        if self.total_call_duration is not None:
            result['TotalCallDuration'] = self.total_call_duration
        if self.video_call_duration is not None:
            result['VideoCallDuration'] = self.video_call_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioCallDuration') is not None:
            self.audio_call_duration = m.get('AudioCallDuration')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')
        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')
        return self


class DescribeUsageDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_stat_list: List[DescribeUsageDistributionStatDataResponseBodyUsageStatList] = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 用量统计数据列表
        self.usage_stat_list = usage_stat_list

    def validate(self):
        if self.usage_stat_list:
            for k in self.usage_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageStatList'] = []
        if self.usage_stat_list is not None:
            for k in self.usage_stat_list:
                result['UsageStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_stat_list = []
        if m.get('UsageStatList') is not None:
            for k in m.get('UsageStatList'):
                temp_model = DescribeUsageDistributionStatDataResponseBodyUsageStatList()
                self.usage_stat_list.append(temp_model.from_map(k))
        return self


class DescribeUsageDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUsageDistributionStatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUsageDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageOsSdkVersionDistributionStatDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
    ):
        # APP ID
        self.app_id = app_id
        # 结束时间，秒级时间戳：1609344000
        self.end_date = end_date
        # 开始时间，秒级时间戳：1609344000
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeUsageOsSdkVersionDistributionStatDataResponseBodyUsageOsSdkVersionStatList(TeaModel):
    def __init__(
        self,
        audio_call_duration: int = None,
        call_duration_ratio: str = None,
        name: str = None,
        os: str = None,
        total_call_duration: int = None,
        video_call_duration: int = None,
    ):
        # 音频通话时长，单位分钟
        self.audio_call_duration = audio_call_duration
        # 通话时长占比，四位小数表示，如1.0000
        self.call_duration_ratio = call_duration_ratio
        # SDK版本名称，1.0.0、1.1.1等
        self.name = name
        # 操作系统，如iOS、android等
        self.os = os
        # 总通话时长，单位分钟
        self.total_call_duration = total_call_duration
        # 视频通话时长，单位分钟
        self.video_call_duration = video_call_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_call_duration is not None:
            result['AudioCallDuration'] = self.audio_call_duration
        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio
        if self.name is not None:
            result['Name'] = self.name
        if self.os is not None:
            result['Os'] = self.os
        if self.total_call_duration is not None:
            result['TotalCallDuration'] = self.total_call_duration
        if self.video_call_duration is not None:
            result['VideoCallDuration'] = self.video_call_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioCallDuration') is not None:
            self.audio_call_duration = m.get('AudioCallDuration')
        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')
        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')
        return self


class DescribeUsageOsSdkVersionDistributionStatDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_os_sdk_version_stat_list: List[DescribeUsageOsSdkVersionDistributionStatDataResponseBodyUsageOsSdkVersionStatList] = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 用量统计SDK版本数据列表
        self.usage_os_sdk_version_stat_list = usage_os_sdk_version_stat_list

    def validate(self):
        if self.usage_os_sdk_version_stat_list:
            for k in self.usage_os_sdk_version_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageOsSdkVersionStatList'] = []
        if self.usage_os_sdk_version_stat_list is not None:
            for k in self.usage_os_sdk_version_stat_list:
                result['UsageOsSdkVersionStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_os_sdk_version_stat_list = []
        if m.get('UsageOsSdkVersionStatList') is not None:
            for k in m.get('UsageOsSdkVersionStatList'):
                temp_model = DescribeUsageOsSdkVersionDistributionStatDataResponseBodyUsageOsSdkVersionStatList()
                self.usage_os_sdk_version_stat_list.append(temp_model.from_map(k))
        return self


class DescribeUsageOsSdkVersionDistributionStatDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUsageOsSdkVersionDistributionStatDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUsageOsSdkVersionDistributionStatDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageOverallDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        types: str = None,
    ):
        # APP ID
        self.app_id = app_id
        # 结束时间，秒级时间戳：1609344000
        self.end_date = end_date
        # 开始时间，秒级时间戳：1609344000
        self.start_date = start_date
        # 类型，半角逗号分隔    总时长：TOTAL_CALL_DURATION  视频通信时长：VIDEO_CALL_DURATION  音频通信时长：AUDIO_CALL_DURATION    通信频道数：CALL_CHANNEL_COUNT  高并发通信频道数：  HIGHLY_CONCURRENT_CHANNEL_COUNT  并发频道数峰值：  CHANNEL_CONCURRENT_PEAK    在线人数峰值：ONLINE_USER_PEAK  累计通话人数：  TOTAL_CALL_USER  累计进出人次：  TOTAL_INOUT_NUM
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class DescribeUsageOverallDataResponseBodyUsageOverallDataNodes(TeaModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        # x轴横坐标
        self.x = x
        # y轴横坐标
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeUsageOverallDataResponseBodyUsageOverallData(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeUsageOverallDataResponseBodyUsageOverallDataNodes] = None,
        type: str = None,
    ):
        # 坐标点列表
        self.nodes = nodes
        # 类型，半角逗号分隔    总时长：TOTAL_CALL_DURATION  视频通信时长：VIDEO_CALL_DURATION  音频通信时长：AUDIO_CALL_DURATION    通信频道数：CALL_CHANNEL_COUNT  高并发通信频道数：  HIGHLY_CONCURRENT_CHANNEL_COUNT  并发频道数峰值：  CHANNEL_CONCURRENT_PEAK    在线人数峰值：ONLINE_USER_PEAK  累计通话人数：  TOTAL_CALL_USER  累计进出人次：  TOTAL_INOUT_NUM
        self.type = type

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeUsageOverallDataResponseBodyUsageOverallDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeUsageOverallDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usage_overall_data: List[DescribeUsageOverallDataResponseBodyUsageOverallData] = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 用量概览数据列表
        self.usage_overall_data = usage_overall_data

    def validate(self):
        if self.usage_overall_data:
            for k in self.usage_overall_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UsageOverallData'] = []
        if self.usage_overall_data is not None:
            for k in self.usage_overall_data:
                result['UsageOverallData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.usage_overall_data = []
        if m.get('UsageOverallData') is not None:
            for k in m.get('UsageOverallData'):
                temp_model = DescribeUsageOverallDataResponseBodyUsageOverallData()
                self.usage_overall_data.append(temp_model.from_map(k))
        return self


class DescribeUsageOverallDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUsageOverallDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUsageOverallDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppExpMetricRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        rule: str = None,
    ):
        # APP ID
        self.app_id = app_id
        # 具体规则，JSON格式
        self.rule = rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.rule is not None:
            result['Rule'] = self.rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        return self


class UpdateAppExpMetricRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppExpMetricRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppExpMetricRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAppExpMetricRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppFollowCallRuleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        rule: str = None,
    ):
        # APP ID
        self.app_id = app_id
        # 具体规则，JSON格式
        self.rule = rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.rule is not None:
            result['Rule'] = self.rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        return self


class UpdateAppFollowCallRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppFollowCallRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppFollowCallRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAppFollowCallRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


