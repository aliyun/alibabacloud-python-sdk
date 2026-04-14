# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateChatSessionRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        device_id: str = None,
        instance_id: str = None,
        license: str = None,
        platform: str = None,
    ):
        self.app_id = app_id
        self.device_id = device_id
        # 需要在[数字人实时交互服务](https://common-buy.aliyun.com/?spm=a2c4g.11186623.0.0.457876812ETi6y&commodityCode=avatar_2dchat_public_cn)购买完成对应的服务购买，当前有可用的服务时，前往阿里云-[我的订单](https://billing-cost.console.aliyun.com/order/list)页面对应订单详情下进行查询
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 灵眸平台颁发的个人凭证（在使用端渲染数字人的场景下必填）。
        self.license = license
        # 运行SDK的平台（在使用端渲染数字人的场景下必填）。
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.device_id is not None:
            result['deviceId'] = self.device_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.license is not None:
            result['license'] = self.license

        if self.platform is not None:
            result['platform'] = self.platform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('license') is not None:
            self.license = m.get('license')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        return self

