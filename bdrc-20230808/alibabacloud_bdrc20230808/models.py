# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CheckRulesRequest(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        rule_id: str = None,
    ):
        # This parameter is required.
        self.resource_arn = resource_arn
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CheckRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CheckRulesResponseBody(TeaModel):
    def __init__(
        self,
        data: CheckRulesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CheckRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseBdrcServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class CloseBdrcServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseBdrcServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloseBdrcServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCheckDetailsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_arn: str = None,
        rule_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.resource_arn = resource_arn
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeCheckDetailsResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_time: int = None,
        detail: str = None,
        product_type: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        rule_id: str = None,
        rule_template: str = None,
    ):
        self.check_status = check_status
        self.check_time = check_time
        self.detail = detail
        self.product_type = product_type
        self.resource_arn = resource_arn
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.rule_id = rule_id
        self.rule_template = rule_template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_time is not None:
            result['CheckTime'] = self.check_time
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_template is not None:
            result['RuleTemplate'] = self.rule_template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckTime') is not None:
            self.check_time = m.get('CheckTime')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleTemplate') is not None:
            self.rule_template = m.get('RuleTemplate')
        return self


class DescribeCheckDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        content: List[DescribeCheckDetailsResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.content = content
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeCheckDetailsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCheckDetailsResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeCheckDetailsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeCheckDetailsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCheckDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCheckDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCheckDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProductsResponseBodyDataContentProtectionScoreDistributionRange(TeaModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
    ):
        self.from_ = from_
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class DescribeProductsResponseBodyDataContentProtectionScoreDistribution(TeaModel):
    def __init__(
        self,
        count: int = None,
        range: DescribeProductsResponseBodyDataContentProtectionScoreDistributionRange = None,
    ):
        self.count = count
        self.range = range

    def validate(self):
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.range is not None:
            result['Range'] = self.range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Range') is not None:
            temp_model = DescribeProductsResponseBodyDataContentProtectionScoreDistributionRange()
            self.range = temp_model.from_map(m['Range'])
        return self


class DescribeProductsResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        check_failed_count: int = None,
        check_failed_resource_count: int = None,
        disable_check_resource_count: int = None,
        enable_check: bool = None,
        product_type: str = None,
        protection_score: int = None,
        protection_score_distribution: List[DescribeProductsResponseBodyDataContentProtectionScoreDistribution] = None,
        protection_score_updated_time: int = None,
        risk_count: int = None,
        risky_resource_count: int = None,
        total_resource_count: int = None,
    ):
        self.check_failed_count = check_failed_count
        self.check_failed_resource_count = check_failed_resource_count
        self.disable_check_resource_count = disable_check_resource_count
        self.enable_check = enable_check
        self.product_type = product_type
        self.protection_score = protection_score
        self.protection_score_distribution = protection_score_distribution
        self.protection_score_updated_time = protection_score_updated_time
        self.risk_count = risk_count
        self.risky_resource_count = risky_resource_count
        self.total_resource_count = total_resource_count

    def validate(self):
        if self.protection_score_distribution:
            for k in self.protection_score_distribution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_failed_count is not None:
            result['CheckFailedCount'] = self.check_failed_count
        if self.check_failed_resource_count is not None:
            result['CheckFailedResourceCount'] = self.check_failed_resource_count
        if self.disable_check_resource_count is not None:
            result['DisableCheckResourceCount'] = self.disable_check_resource_count
        if self.enable_check is not None:
            result['EnableCheck'] = self.enable_check
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.protection_score is not None:
            result['ProtectionScore'] = self.protection_score
        result['ProtectionScoreDistribution'] = []
        if self.protection_score_distribution is not None:
            for k in self.protection_score_distribution:
                result['ProtectionScoreDistribution'].append(k.to_map() if k else None)
        if self.protection_score_updated_time is not None:
            result['ProtectionScoreUpdatedTime'] = self.protection_score_updated_time
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.risky_resource_count is not None:
            result['RiskyResourceCount'] = self.risky_resource_count
        if self.total_resource_count is not None:
            result['TotalResourceCount'] = self.total_resource_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckFailedCount') is not None:
            self.check_failed_count = m.get('CheckFailedCount')
        if m.get('CheckFailedResourceCount') is not None:
            self.check_failed_resource_count = m.get('CheckFailedResourceCount')
        if m.get('DisableCheckResourceCount') is not None:
            self.disable_check_resource_count = m.get('DisableCheckResourceCount')
        if m.get('EnableCheck') is not None:
            self.enable_check = m.get('EnableCheck')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProtectionScore') is not None:
            self.protection_score = m.get('ProtectionScore')
        self.protection_score_distribution = []
        if m.get('ProtectionScoreDistribution') is not None:
            for k in m.get('ProtectionScoreDistribution'):
                temp_model = DescribeProductsResponseBodyDataContentProtectionScoreDistribution()
                self.protection_score_distribution.append(temp_model.from_map(k))
        if m.get('ProtectionScoreUpdatedTime') is not None:
            self.protection_score_updated_time = m.get('ProtectionScoreUpdatedTime')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('RiskyResourceCount') is not None:
            self.risky_resource_count = m.get('RiskyResourceCount')
        if m.get('TotalResourceCount') is not None:
            self.total_resource_count = m.get('TotalResourceCount')
        return self


class DescribeProductsResponseBodyData(TeaModel):
    def __init__(
        self,
        content: List[DescribeProductsResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.content = content
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeProductsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeProductsResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeProductsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeProductsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProductsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourcesRequest(TeaModel):
    def __init__(
        self,
        failed_rule_template: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_id: str = None,
        resource_type: str = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        self.failed_rule_template = failed_rule_template
        self.max_results = max_results
        self.next_token = next_token
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.sort_by = sort_by
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_rule_template is not None:
            result['FailedRuleTemplate'] = self.failed_rule_template
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedRuleTemplate') is not None:
            self.failed_rule_template = m.get('FailedRuleTemplate')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class DescribeResourcesResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        archive_data_size: int = None,
        check_failed_count: int = None,
        cold_archive_data_size: int = None,
        create_time: int = None,
        enable_check: bool = None,
        ia_data_size: int = None,
        product_type: str = None,
        protection_score: int = None,
        protection_score_updated_time: int = None,
        region_id: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        risk_count: int = None,
        standard_data_size: int = None,
        status: str = None,
        total_data_size: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.archive_data_size = archive_data_size
        self.check_failed_count = check_failed_count
        self.cold_archive_data_size = cold_archive_data_size
        self.create_time = create_time
        self.enable_check = enable_check
        self.ia_data_size = ia_data_size
        self.product_type = product_type
        self.protection_score = protection_score
        self.protection_score_updated_time = protection_score_updated_time
        self.region_id = region_id
        self.resource_arn = resource_arn
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.risk_count = risk_count
        self.standard_data_size = standard_data_size
        self.status = status
        self.total_data_size = total_data_size
        # vSwitch ID
        self.v_switch_id = v_switch_id
        # vpc ID
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_data_size is not None:
            result['ArchiveDataSize'] = self.archive_data_size
        if self.check_failed_count is not None:
            result['CheckFailedCount'] = self.check_failed_count
        if self.cold_archive_data_size is not None:
            result['ColdArchiveDataSize'] = self.cold_archive_data_size
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_check is not None:
            result['EnableCheck'] = self.enable_check
        if self.ia_data_size is not None:
            result['IaDataSize'] = self.ia_data_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.protection_score is not None:
            result['ProtectionScore'] = self.protection_score
        if self.protection_score_updated_time is not None:
            result['ProtectionScoreUpdatedTime'] = self.protection_score_updated_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.standard_data_size is not None:
            result['StandardDataSize'] = self.standard_data_size
        if self.status is not None:
            result['Status'] = self.status
        if self.total_data_size is not None:
            result['TotalDataSize'] = self.total_data_size
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveDataSize') is not None:
            self.archive_data_size = m.get('ArchiveDataSize')
        if m.get('CheckFailedCount') is not None:
            self.check_failed_count = m.get('CheckFailedCount')
        if m.get('ColdArchiveDataSize') is not None:
            self.cold_archive_data_size = m.get('ColdArchiveDataSize')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableCheck') is not None:
            self.enable_check = m.get('EnableCheck')
        if m.get('IaDataSize') is not None:
            self.ia_data_size = m.get('IaDataSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProtectionScore') is not None:
            self.protection_score = m.get('ProtectionScore')
        if m.get('ProtectionScoreUpdatedTime') is not None:
            self.protection_score_updated_time = m.get('ProtectionScoreUpdatedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('StandardDataSize') is not None:
            self.standard_data_size = m.get('StandardDataSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalDataSize') is not None:
            self.total_data_size = m.get('TotalDataSize')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        content: List[DescribeResourcesResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.content = content
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeResourcesResponseBodyDataContent()
                self.content.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRulesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_type: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeRulesResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        check_failed_resource_count: int = None,
        check_status: str = None,
        check_time: int = None,
        product_type: str = None,
        resource_type: str = None,
        risky_resource_count: int = None,
        rule_id: str = None,
        rule_template: str = None,
        total_resource_count: int = None,
    ):
        self.check_failed_resource_count = check_failed_resource_count
        self.check_status = check_status
        self.check_time = check_time
        self.product_type = product_type
        self.resource_type = resource_type
        self.risky_resource_count = risky_resource_count
        self.rule_id = rule_id
        self.rule_template = rule_template
        self.total_resource_count = total_resource_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_failed_resource_count is not None:
            result['CheckFailedResourceCount'] = self.check_failed_resource_count
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_time is not None:
            result['CheckTime'] = self.check_time
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.risky_resource_count is not None:
            result['RiskyResourceCount'] = self.risky_resource_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_template is not None:
            result['RuleTemplate'] = self.rule_template
        if self.total_resource_count is not None:
            result['TotalResourceCount'] = self.total_resource_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckFailedResourceCount') is not None:
            self.check_failed_resource_count = m.get('CheckFailedResourceCount')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckTime') is not None:
            self.check_time = m.get('CheckTime')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RiskyResourceCount') is not None:
            self.risky_resource_count = m.get('RiskyResourceCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleTemplate') is not None:
            self.rule_template = m.get('RuleTemplate')
        if m.get('TotalResourceCount') is not None:
            self.total_resource_count = m.get('TotalResourceCount')
        return self


class DescribeRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        content: List[DescribeRulesResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.content = content
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeRulesResponseBodyDataContent()
                self.content.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRulesResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeRulesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        complete_time: int = None,
        error_message: str = None,
        execution_id: str = None,
        expire_time: int = None,
        progress: int = None,
        request_id: str = None,
        start_time: int = None,
        task_description: str = None,
        task_detail: str = None,
        task_id: str = None,
        task_name: str = None,
        task_priority: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        self.complete_time = complete_time
        self.error_message = error_message
        self.execution_id = execution_id
        self.expire_time = expire_time
        self.progress = progress
        self.request_id = request_id
        self.start_time = start_time
        self.task_description = task_description
        self.task_detail = task_detail
        self.task_id = task_id
        self.task_name = task_name
        self.task_priority = task_priority
        self.task_status = task_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_description is not None:
            result['TaskDescription'] = self.task_description
        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_priority is not None:
            result['TaskPriority'] = self.task_priority
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskDescription') is not None:
            self.task_description = m.get('TaskDescription')
        if m.get('TaskDetail') is not None:
            self.task_detail = m.get('TaskDetail')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskPriority') is not None:
            self.task_priority = m.get('TaskPriority')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        task_status: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class DescribeTasksResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        complete_time: int = None,
        error_message: str = None,
        execution_id: str = None,
        expire_time: int = None,
        progress: int = None,
        request_id: str = None,
        start_time: int = None,
        task_description: str = None,
        task_detail: str = None,
        task_id: str = None,
        task_name: str = None,
        task_priority: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        self.complete_time = complete_time
        self.error_message = error_message
        self.execution_id = execution_id
        self.expire_time = expire_time
        self.progress = progress
        self.request_id = request_id
        self.start_time = start_time
        self.task_description = task_description
        self.task_detail = task_detail
        self.task_id = task_id
        self.task_name = task_name
        self.task_priority = task_priority
        self.task_status = task_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_description is not None:
            result['TaskDescription'] = self.task_description
        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_priority is not None:
            result['TaskPriority'] = self.task_priority
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskDescription') is not None:
            self.task_description = m.get('TaskDescription')
        if m.get('TaskDetail') is not None:
            self.task_detail = m.get('TaskDetail')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskPriority') is not None:
            self.task_priority = m.get('TaskPriority')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        content: List[DescribeTasksResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.content = content
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeTasksResponseBodyDataContent()
                self.content.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeTasksResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopRiskyResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeTopRiskyResourcesResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        archive_data_size: int = None,
        check_failed_count: int = None,
        cold_archive_data_size: int = None,
        create_time: int = None,
        enable_check: bool = None,
        ia_data_size: int = None,
        product_type: str = None,
        protection_score: int = None,
        protection_score_updated_time: int = None,
        region_id: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        risk_count: int = None,
        standard_data_size: int = None,
        status: str = None,
        total_data_size: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.archive_data_size = archive_data_size
        self.check_failed_count = check_failed_count
        self.cold_archive_data_size = cold_archive_data_size
        self.create_time = create_time
        self.enable_check = enable_check
        self.ia_data_size = ia_data_size
        self.product_type = product_type
        self.protection_score = protection_score
        self.protection_score_updated_time = protection_score_updated_time
        self.region_id = region_id
        self.resource_arn = resource_arn
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.risk_count = risk_count
        self.standard_data_size = standard_data_size
        self.status = status
        self.total_data_size = total_data_size
        # vSwitch ID
        self.v_switch_id = v_switch_id
        # vpc ID
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_data_size is not None:
            result['ArchiveDataSize'] = self.archive_data_size
        if self.check_failed_count is not None:
            result['CheckFailedCount'] = self.check_failed_count
        if self.cold_archive_data_size is not None:
            result['ColdArchiveDataSize'] = self.cold_archive_data_size
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_check is not None:
            result['EnableCheck'] = self.enable_check
        if self.ia_data_size is not None:
            result['IaDataSize'] = self.ia_data_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.protection_score is not None:
            result['ProtectionScore'] = self.protection_score
        if self.protection_score_updated_time is not None:
            result['ProtectionScoreUpdatedTime'] = self.protection_score_updated_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.standard_data_size is not None:
            result['StandardDataSize'] = self.standard_data_size
        if self.status is not None:
            result['Status'] = self.status
        if self.total_data_size is not None:
            result['TotalDataSize'] = self.total_data_size
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveDataSize') is not None:
            self.archive_data_size = m.get('ArchiveDataSize')
        if m.get('CheckFailedCount') is not None:
            self.check_failed_count = m.get('CheckFailedCount')
        if m.get('ColdArchiveDataSize') is not None:
            self.cold_archive_data_size = m.get('ColdArchiveDataSize')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableCheck') is not None:
            self.enable_check = m.get('EnableCheck')
        if m.get('IaDataSize') is not None:
            self.ia_data_size = m.get('IaDataSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProtectionScore') is not None:
            self.protection_score = m.get('ProtectionScore')
        if m.get('ProtectionScoreUpdatedTime') is not None:
            self.protection_score_updated_time = m.get('ProtectionScoreUpdatedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('StandardDataSize') is not None:
            self.standard_data_size = m.get('StandardDataSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalDataSize') is not None:
            self.total_data_size = m.get('TotalDataSize')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeTopRiskyResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        content: List[DescribeTopRiskyResourcesResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.content = content
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeTopRiskyResourcesResponseBodyDataContent()
                self.content.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTopRiskyResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeTopRiskyResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeTopRiskyResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTopRiskyResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTopRiskyResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTopRiskyResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableCheckProductRequest(TeaModel):
    def __init__(
        self,
        product_type: str = None,
    ):
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DisableCheckProductResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DisableCheckProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableCheckProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableCheckProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableCheckResourceRequest(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
    ):
        # This parameter is required.
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        return self


class DisableCheckResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DisableCheckResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableCheckResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableCheckResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableCheckProductRequest(TeaModel):
    def __init__(
        self,
        product_type: str = None,
    ):
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class EnableCheckProductResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class EnableCheckProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableCheckProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableCheckProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableCheckResourceRequest(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
    ):
        # This parameter is required.
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        return self


class EnableCheckResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class EnableCheckResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableCheckResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableCheckResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBdrcServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        open_time: int = None,
        protection_score_updated_time: int = None,
        service_initialize_status: str = None,
        service_status: str = None,
    ):
        self.open_time = open_time
        self.protection_score_updated_time = protection_score_updated_time
        self.service_initialize_status = service_initialize_status
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        if self.protection_score_updated_time is not None:
            result['ProtectionScoreUpdatedTime'] = self.protection_score_updated_time
        if self.service_initialize_status is not None:
            result['ServiceInitializeStatus'] = self.service_initialize_status
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        if m.get('ProtectionScoreUpdatedTime') is not None:
            self.protection_score_updated_time = m.get('ProtectionScoreUpdatedTime')
        if m.get('ServiceInitializeStatus') is not None:
            self.service_initialize_status = m.get('ServiceInitializeStatus')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class GetBdrcServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: GetBdrcServiceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetBdrcServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBdrcServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBdrcServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBdrcServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenBdrcServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class OpenBdrcServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenBdrcServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenBdrcServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class UpdateResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


