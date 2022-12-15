# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class LingJieApiInvokeCountMetrics(TeaModel):
    def __init__(
        self,
        count: int = None,
        day: str = None,
        hour: str = None,
    ):
        self.count = count
        self.day = day
        self.hour = hour

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        return self


class LingJieApiInvokeCount(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        metrics: List[LingJieApiInvokeCountMetrics] = None,
        project_id: str = None,
        region: str = None,
        statistics_unit: str = None,
        time_unit: str = None,
    ):
        self.api_name = api_name
        self.metrics = metrics
        self.project_id = project_id
        self.region = region
        self.statistics_unit = statistics_unit
        self.time_unit = time_unit

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
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region is not None:
            result['Region'] = self.region
        if self.statistics_unit is not None:
            result['StatisticsUnit'] = self.statistics_unit
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = LingJieApiInvokeCountMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StatisticsUnit') is not None:
            self.statistics_unit = m.get('StatisticsUnit')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class LingJieApiInvokeQpsMetrics(TeaModel):
    def __init__(
        self,
        day: str = None,
        hour: str = None,
        max_qps: int = None,
    ):
        self.day = day
        self.hour = hour
        self.max_qps = max_qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        return self


class LingJieApiInvokeQps(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        metrics: List[LingJieApiInvokeQpsMetrics] = None,
        project_id: str = None,
        region: str = None,
        statistics_unit: str = None,
        time_unit: str = None,
    ):
        self.api_name = api_name
        self.metrics = metrics
        self.project_id = project_id
        self.region = region
        self.statistics_unit = statistics_unit
        self.time_unit = time_unit

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
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region is not None:
            result['Region'] = self.region
        if self.statistics_unit is not None:
            result['StatisticsUnit'] = self.statistics_unit
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = LingJieApiInvokeQpsMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StatisticsUnit') is not None:
            self.statistics_unit = m.get('StatisticsUnit')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class LingJieOpenStatusCommoditiesOpenStatus(TeaModel):
    def __init__(
        self,
        cn_name: str = None,
        commodity: str = None,
        describe: str = None,
        detail_page: str = None,
        open: bool = None,
        open_time: str = None,
    ):
        self.cn_name = cn_name
        self.commodity = commodity
        self.describe = describe
        self.detail_page = detail_page
        self.open = open
        self.open_time = open_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_name is not None:
            result['CnName'] = self.cn_name
        if self.commodity is not None:
            result['Commodity'] = self.commodity
        if self.describe is not None:
            result['Describe'] = self.describe
        if self.detail_page is not None:
            result['DetailPage'] = self.detail_page
        if self.open is not None:
            result['Open'] = self.open
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')
        if m.get('Describe') is not None:
            self.describe = m.get('Describe')
        if m.get('DetailPage') is not None:
            self.detail_page = m.get('DetailPage')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        return self


class LingJieOpenStatus(TeaModel):
    def __init__(
        self,
        commodities_open_status: List[LingJieOpenStatusCommoditiesOpenStatus] = None,
        open_time: str = None,
        product_console_url: str = None,
        product_enabled: bool = None,
        product_monitor_url: str = None,
        product_wiki_url: str = None,
    ):
        self.commodities_open_status = commodities_open_status
        self.open_time = open_time
        self.product_console_url = product_console_url
        self.product_enabled = product_enabled
        self.product_monitor_url = product_monitor_url
        self.product_wiki_url = product_wiki_url

    def validate(self):
        if self.commodities_open_status:
            for k in self.commodities_open_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommoditiesOpenStatus'] = []
        if self.commodities_open_status is not None:
            for k in self.commodities_open_status:
                result['CommoditiesOpenStatus'].append(k.to_map() if k else None)
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        if self.product_console_url is not None:
            result['ProductConsoleUrl'] = self.product_console_url
        if self.product_enabled is not None:
            result['ProductEnabled'] = self.product_enabled
        if self.product_monitor_url is not None:
            result['ProductMonitorUrl'] = self.product_monitor_url
        if self.product_wiki_url is not None:
            result['ProductWikiUrl'] = self.product_wiki_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodities_open_status = []
        if m.get('CommoditiesOpenStatus') is not None:
            for k in m.get('CommoditiesOpenStatus'):
                temp_model = LingJieOpenStatusCommoditiesOpenStatus()
                self.commodities_open_status.append(temp_model.from_map(k))
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        if m.get('ProductConsoleUrl') is not None:
            self.product_console_url = m.get('ProductConsoleUrl')
        if m.get('ProductEnabled') is not None:
            self.product_enabled = m.get('ProductEnabled')
        if m.get('ProductMonitorUrl') is not None:
            self.product_monitor_url = m.get('ProductMonitorUrl')
        if m.get('ProductWikiUrl') is not None:
            self.product_wiki_url = m.get('ProductWikiUrl')
        return self


class LingJieOpenStatusDetailApiListMoreOperations(TeaModel):
    def __init__(
        self,
        click_url: str = None,
        operation: str = None,
    ):
        self.click_url = click_url
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.click_url is not None:
            result['ClickUrl'] = self.click_url
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClickUrl') is not None:
            self.click_url = m.get('ClickUrl')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class LingJieOpenStatusDetailApiList(TeaModel):
    def __init__(
        self,
        cn_name: str = None,
        concurrent_limit: str = None,
        en_name: str = None,
        more_operations: List[LingJieOpenStatusDetailApiListMoreOperations] = None,
        statistics_unit: str = None,
        status: str = None,
        usage: str = None,
    ):
        self.cn_name = cn_name
        self.concurrent_limit = concurrent_limit
        self.en_name = en_name
        self.more_operations = more_operations
        self.statistics_unit = statistics_unit
        self.status = status
        self.usage = usage

    def validate(self):
        if self.more_operations:
            for k in self.more_operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_name is not None:
            result['CnName'] = self.cn_name
        if self.concurrent_limit is not None:
            result['ConcurrentLimit'] = self.concurrent_limit
        if self.en_name is not None:
            result['EnName'] = self.en_name
        result['MoreOperations'] = []
        if self.more_operations is not None:
            for k in self.more_operations:
                result['MoreOperations'].append(k.to_map() if k else None)
        if self.statistics_unit is not None:
            result['StatisticsUnit'] = self.statistics_unit
        if self.status is not None:
            result['Status'] = self.status
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')
        if m.get('ConcurrentLimit') is not None:
            self.concurrent_limit = m.get('ConcurrentLimit')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        self.more_operations = []
        if m.get('MoreOperations') is not None:
            for k in m.get('MoreOperations'):
                temp_model = LingJieOpenStatusDetailApiListMoreOperations()
                self.more_operations.append(temp_model.from_map(k))
        if m.get('StatisticsUnit') is not None:
            self.statistics_unit = m.get('StatisticsUnit')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class LingJieOpenStatusDetail(TeaModel):
    def __init__(
        self,
        api_list: List[LingJieOpenStatusDetailApiList] = None,
        commodity_concurrent_limit_tips: str = None,
        commodity_has_open: bool = None,
        commodity_open_url: str = None,
        commodity_usage_tips: str = None,
        user_stop_mode: bool = None,
    ):
        self.api_list = api_list
        self.commodity_concurrent_limit_tips = commodity_concurrent_limit_tips
        self.commodity_has_open = commodity_has_open
        self.commodity_open_url = commodity_open_url
        self.commodity_usage_tips = commodity_usage_tips
        self.user_stop_mode = user_stop_mode

    def validate(self):
        if self.api_list:
            for k in self.api_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiList'] = []
        if self.api_list is not None:
            for k in self.api_list:
                result['ApiList'].append(k.to_map() if k else None)
        if self.commodity_concurrent_limit_tips is not None:
            result['CommodityConcurrentLimitTips'] = self.commodity_concurrent_limit_tips
        if self.commodity_has_open is not None:
            result['CommodityHasOpen'] = self.commodity_has_open
        if self.commodity_open_url is not None:
            result['CommodityOpenUrl'] = self.commodity_open_url
        if self.commodity_usage_tips is not None:
            result['CommodityUsageTips'] = self.commodity_usage_tips
        if self.user_stop_mode is not None:
            result['UserStopMode'] = self.user_stop_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_list = []
        if m.get('ApiList') is not None:
            for k in m.get('ApiList'):
                temp_model = LingJieOpenStatusDetailApiList()
                self.api_list.append(temp_model.from_map(k))
        if m.get('CommodityConcurrentLimitTips') is not None:
            self.commodity_concurrent_limit_tips = m.get('CommodityConcurrentLimitTips')
        if m.get('CommodityHasOpen') is not None:
            self.commodity_has_open = m.get('CommodityHasOpen')
        if m.get('CommodityOpenUrl') is not None:
            self.commodity_open_url = m.get('CommodityOpenUrl')
        if m.get('CommodityUsageTips') is not None:
            self.commodity_usage_tips = m.get('CommodityUsageTips')
        if m.get('UserStopMode') is not None:
            self.user_stop_mode = m.get('UserStopMode')
        return self


class News(TeaModel):
    def __init__(
        self,
        content: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        last: bool = None,
        pic: str = None,
        sort: int = None,
        status: int = None,
        tags: str = None,
        title: str = None,
        type: int = None,
        url: str = None,
    ):
        self.content = content
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.last = last
        self.pic = pic
        self.sort = sort
        self.status = status
        self.tags = tags
        self.title = title
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.last is not None:
            result['Last'] = self.last
        if self.pic is not None:
            result['Pic'] = self.pic
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Last') is not None:
            self.last = m.get('Last')
        if m.get('Pic') is not None:
            self.pic = m.get('Pic')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UserQpsDetail(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        day: str = None,
        qps: int = None,
        qps_rule: str = None,
        status: int = None,
    ):
        self.api_name = api_name
        self.day = day
        self.qps = qps
        self.qps_rule = qps_rule
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.day is not None:
            result['Day'] = self.day
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.qps_rule is not None:
            result['QpsRule'] = self.qps_rule
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('QpsRule') is not None:
            self.qps_rule = m.get('QpsRule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateSDKInstanceRequest(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        pk: str = None,
        platform: str = None,
        recipe: str = None,
        valid_from: int = None,
        valid_to: int = None,
    ):
        self.bundle_id = bundle_id
        self.pk = pk
        self.platform = platform
        self.recipe = recipe
        self.valid_from = valid_from
        self.valid_to = valid_to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.recipe is not None:
            result['Recipe'] = self.recipe
        if self.valid_from is not None:
            result['ValidFrom'] = self.valid_from
        if self.valid_to is not None:
            result['ValidTo'] = self.valid_to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Recipe') is not None:
            self.recipe = m.get('Recipe')
        if m.get('ValidFrom') is not None:
            self.valid_from = m.get('ValidFrom')
        if m.get('ValidTo') is not None:
            self.valid_to = m.get('ValidTo')
        return self


class CreateSDKInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_message: str = None,
        http_code: int = None,
        ok: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.http_code = http_code
        self.ok = ok
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.ok is not None:
            result['Ok'] = self.ok
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Ok') is not None:
            self.ok = m.get('Ok')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSDKInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSDKInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateSDKInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSDKInstanceDebugInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetSDKInstanceDebugInfoResponseBodyDataEvents(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: int = None,
        success: bool = None,
        time_stamp: str = None,
    ):
        self.content = content
        self.id = id
        self.success = success
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.success is not None:
            result['Success'] = self.success
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class GetSDKInstanceDebugInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        created_at: str = None,
        events: List[GetSDKInstanceDebugInfoResponseBodyDataEvents] = None,
        instance_id: str = None,
        latest_build: str = None,
        platform: str = None,
        recipe: str = None,
        status: str = None,
        updated_at: str = None,
        valid_from_date: str = None,
        valid_to_date: str = None,
    ):
        self.bundle_id = bundle_id
        self.created_at = created_at
        self.events = events
        self.instance_id = instance_id
        self.latest_build = latest_build
        self.platform = platform
        self.recipe = recipe
        self.status = status
        self.updated_at = updated_at
        self.valid_from_date = valid_from_date
        self.valid_to_date = valid_to_date

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
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.latest_build is not None:
            result['LatestBuild'] = self.latest_build
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.recipe is not None:
            result['Recipe'] = self.recipe
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.valid_from_date is not None:
            result['ValidFromDate'] = self.valid_from_date
        if self.valid_to_date is not None:
            result['ValidToDate'] = self.valid_to_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = GetSDKInstanceDebugInfoResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LatestBuild') is not None:
            self.latest_build = m.get('LatestBuild')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Recipe') is not None:
            self.recipe = m.get('Recipe')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('ValidFromDate') is not None:
            self.valid_from_date = m.get('ValidFromDate')
        if m.get('ValidToDate') is not None:
            self.valid_to_date = m.get('ValidToDate')
        return self


class GetSDKInstanceDebugInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSDKInstanceDebugInfoResponseBodyData = None,
        error_message: str = None,
        http_code: int = None,
        ok: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.http_code = http_code
        self.ok = ok
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.ok is not None:
            result['Ok'] = self.ok
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSDKInstanceDebugInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Ok') is not None:
            self.ok = m.get('Ok')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSDKInstanceDebugInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSDKInstanceDebugInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetSDKInstanceDebugInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySDKInstancesRequest(TeaModel):
    def __init__(
        self,
        code_list: str = None,
        created_after_date: str = None,
        created_before_date: str = None,
        page_number: int = None,
        page_size: int = None,
        pk: str = None,
    ):
        self.code_list = code_list
        self.created_after_date = created_after_date
        self.created_before_date = created_before_date
        self.page_number = page_number
        self.page_size = page_size
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_list is not None:
            result['CodeList'] = self.code_list
        if self.created_after_date is not None:
            result['CreatedAfterDate'] = self.created_after_date
        if self.created_before_date is not None:
            result['CreatedBeforeDate'] = self.created_before_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pk is not None:
            result['Pk'] = self.pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeList') is not None:
            self.code_list = m.get('CodeList')
        if m.get('CreatedAfterDate') is not None:
            self.created_after_date = m.get('CreatedAfterDate')
        if m.get('CreatedBeforeDate') is not None:
            self.created_before_date = m.get('CreatedBeforeDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        return self


class QuerySDKInstancesResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        created_at: str = None,
        instance_id: str = None,
        latest_build: str = None,
        platform: str = None,
        recipe: str = None,
        status: str = None,
        updated_at: str = None,
        user_id: str = None,
        valid_from_date: str = None,
        valid_to_date: str = None,
    ):
        self.bundle_id = bundle_id
        self.created_at = created_at
        self.instance_id = instance_id
        self.latest_build = latest_build
        self.platform = platform
        self.recipe = recipe
        self.status = status
        self.updated_at = updated_at
        self.user_id = user_id
        self.valid_from_date = valid_from_date
        self.valid_to_date = valid_to_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.latest_build is not None:
            result['LatestBuild'] = self.latest_build
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.recipe is not None:
            result['Recipe'] = self.recipe
        if self.status is not None:
            result['Status'] = self.status
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.valid_from_date is not None:
            result['ValidFromDate'] = self.valid_from_date
        if self.valid_to_date is not None:
            result['ValidToDate'] = self.valid_to_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LatestBuild') is not None:
            self.latest_build = m.get('LatestBuild')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Recipe') is not None:
            self.recipe = m.get('Recipe')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ValidFromDate') is not None:
            self.valid_from_date = m.get('ValidFromDate')
        if m.get('ValidToDate') is not None:
            self.valid_to_date = m.get('ValidToDate')
        return self


class QuerySDKInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        content: List[QuerySDKInstancesResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.content = content
        self.page_number = page_number
        self.page_size = page_size
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = QuerySDKInstancesResponseBodyDataContent()
                self.content.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySDKInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QuerySDKInstancesResponseBodyData = None,
        error_message: str = None,
        http_code: int = None,
        ok: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.http_code = http_code
        self.ok = ok
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.ok is not None:
            result['Ok'] = self.ok
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QuerySDKInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Ok') is not None:
            self.ok = m.get('Ok')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QuerySDKInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySDKInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QuerySDKInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSDKInstanceProductionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartSDKInstanceProductionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        http_code: int = None,
        ok: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.error_message = error_message
        self.http_code = http_code
        self.ok = ok
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.ok is not None:
            result['Ok'] = self.ok
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Ok') is not None:
            self.ok = m.get('Ok')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartSDKInstanceProductionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartSDKInstanceProductionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartSDKInstanceProductionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


