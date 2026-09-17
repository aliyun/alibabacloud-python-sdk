# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetGatewayResourceQuotaUsageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetGatewayResourceQuotaUsageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # 业务响应码。成功时为 Ok；失败时为具体错误码，应结合 HTTP 状态码处理。
        self.code = code
        # 目标网关及其九项资源配额观测结果。示例数值只说明格式，实际有效上限以本次响应为准。
        self.data = data
        # 失败时返回的错误说明，成功响应通常省略本字段。示例为错误信息，不是成功响应。
        self.message = message
        # 请求的唯一标识，用于排查问题。
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetGatewayResourceQuotaUsageResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGatewayResourceQuotaUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        items: List[main_models.GetGatewayResourceQuotaUsageResponseBodyDataItems] = None,
        observed_at: str = None,
    ):
        # 本次查询的目标网关唯一标识，与请求路径 gatewayId 一致。
        self.gateway_id = gateway_id
        # 固定返回九项，每个 quotaKey 仅出现一次。不适用或暂不展示的项仍保留，applicable=false 且省略 used/limit。不返回剩余额度或百分比；示例数值不是固定默认上限。
        self.items = items
        # 服务端完成本次统计的 UTC 时间，格式为 RFC 3339，可包含小数秒。各来源独立读取，不保证跨来源瞬时原子快照。
        self.observed_at = observed_at

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
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.observed_at is not None:
            result['observedAt'] = self.observed_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetGatewayResourceQuotaUsageResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('observedAt') is not None:
            self.observed_at = m.get('observedAt')

        return self

class GetGatewayResourceQuotaUsageResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        applicable: bool = None,
        limit: int = None,
        limit_scope: str = None,
        quota_key: str = None,
        used: int = None,
        used_scope: str = None,
    ):
        # true 时返回 used 和 limit；false 时省略二者。CustomPlugin 当前固定为 false，仅表示暂时隐藏配额展示，不影响插件上传、安装或既有配额校验。其他项按网关能力及有效额度判定，不能仅凭本字段推断写入操作是否允许。
        self.applicable = applicable
        # 当前生效的非负整数配额上限，单位与 used 相同，已考虑现有配置、加白及适用的购买额度。仅 applicable=true 时返回，包括合法零值；示例不是所有网关的固定上限。
        self.limit = limit
        # GATEWAY 表示当前网关；ACCOUNT_GATEWAY_TYPE 表示当前账号、地域及网关类型的范围。仅 CustomPlugin 保留 ACCOUNT_GATEWAY_TYPE 标识；该项当前不读取或返回上限。
        self.limit_scope = limit_scope
        # 指标标识：Route（路由）、ConsumerAuthorizationRule（消费者授权规则）、McpServer（MCP Server）、Domain（域名）、Service（服务）、ConsumerQuotaRule（消费者配额规则）、K8sServiceSource（K8s 服务来源）、InstalledPlugin（已安装插件）、CustomPlugin（自定义插件）。
        self.quota_key = quota_key
        # 实际占用数量，为非负整数，单位与 quotaKey 对应。仅 applicable=true 时返回；零值为真实零用量，历史超额可大于 limit，不截断。
        self.used = used
        # GATEWAY 表示当前网关；ACCOUNT_REGION 表示当前账号在当前地域的共享范围。仅 CustomPlugin 保留 ACCOUNT_REGION 标识；该项当前不读取或返回用量。
        self.used_scope = used_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicable is not None:
            result['applicable'] = self.applicable

        if self.limit is not None:
            result['limit'] = self.limit

        if self.limit_scope is not None:
            result['limitScope'] = self.limit_scope

        if self.quota_key is not None:
            result['quotaKey'] = self.quota_key

        if self.used is not None:
            result['used'] = self.used

        if self.used_scope is not None:
            result['usedScope'] = self.used_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicable') is not None:
            self.applicable = m.get('applicable')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('limitScope') is not None:
            self.limit_scope = m.get('limitScope')

        if m.get('quotaKey') is not None:
            self.quota_key = m.get('quotaKey')

        if m.get('used') is not None:
            self.used = m.get('used')

        if m.get('usedScope') is not None:
            self.used_scope = m.get('usedScope')

        return self

