# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUnionTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        anchor_id: str = None,
        brand_user_id: int = None,
        brand_user_nick: str = None,
        channel: str = None,
        channel_id: str = None,
        charge_ploy: int = None,
        charge_type: int = None,
        client_token: str = None,
        content_id: int = None,
        content_url: str = None,
        custom_creative_type: str = None,
        end_time: str = None,
        industry_label_bag_id: int = None,
        media_id_black_list_shrink: str = None,
        media_id_white_list_shrink: str = None,
        media_industry: str = None,
        name: str = None,
        optimization_switch: int = None,
        proxy_user_id: int = None,
        quota: int = None,
        quota_day: int = None,
        start_time: str = None,
        task_biz_type: str = None,
        task_rule_type: str = None,
        task_type: str = None,
    ):
        self.anchor_id = anchor_id
        self.brand_user_id = brand_user_id
        self.brand_user_nick = brand_user_nick
        self.channel = channel
        self.channel_id = channel_id
        self.charge_ploy = charge_ploy
        self.charge_type = charge_type
        self.client_token = client_token
        self.content_id = content_id
        self.content_url = content_url
        self.custom_creative_type = custom_creative_type
        self.end_time = end_time
        self.industry_label_bag_id = industry_label_bag_id
        self.media_id_black_list_shrink = media_id_black_list_shrink
        self.media_id_white_list_shrink = media_id_white_list_shrink
        self.media_industry = media_industry
        self.name = name
        self.optimization_switch = optimization_switch
        self.proxy_user_id = proxy_user_id
        self.quota = quota
        self.quota_day = quota_day
        self.start_time = start_time
        self.task_biz_type = task_biz_type
        self.task_rule_type = task_rule_type
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id

        if self.brand_user_id is not None:
            result['BrandUserId'] = self.brand_user_id

        if self.brand_user_nick is not None:
            result['BrandUserNick'] = self.brand_user_nick

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.charge_ploy is not None:
            result['ChargePloy'] = self.charge_ploy

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content_id is not None:
            result['ContentId'] = self.content_id

        if self.content_url is not None:
            result['ContentUrl'] = self.content_url

        if self.custom_creative_type is not None:
            result['CustomCreativeType'] = self.custom_creative_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.industry_label_bag_id is not None:
            result['IndustryLabelBagId'] = self.industry_label_bag_id

        if self.media_id_black_list_shrink is not None:
            result['MediaIdBlackList'] = self.media_id_black_list_shrink

        if self.media_id_white_list_shrink is not None:
            result['MediaIdWhiteList'] = self.media_id_white_list_shrink

        if self.media_industry is not None:
            result['MediaIndustry'] = self.media_industry

        if self.name is not None:
            result['Name'] = self.name

        if self.optimization_switch is not None:
            result['OptimizationSwitch'] = self.optimization_switch

        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.quota_day is not None:
            result['QuotaDay'] = self.quota_day

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_biz_type is not None:
            result['TaskBizType'] = self.task_biz_type

        if self.task_rule_type is not None:
            result['TaskRuleType'] = self.task_rule_type

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')

        if m.get('BrandUserId') is not None:
            self.brand_user_id = m.get('BrandUserId')

        if m.get('BrandUserNick') is not None:
            self.brand_user_nick = m.get('BrandUserNick')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChargePloy') is not None:
            self.charge_ploy = m.get('ChargePloy')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')

        if m.get('ContentUrl') is not None:
            self.content_url = m.get('ContentUrl')

        if m.get('CustomCreativeType') is not None:
            self.custom_creative_type = m.get('CustomCreativeType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IndustryLabelBagId') is not None:
            self.industry_label_bag_id = m.get('IndustryLabelBagId')

        if m.get('MediaIdBlackList') is not None:
            self.media_id_black_list_shrink = m.get('MediaIdBlackList')

        if m.get('MediaIdWhiteList') is not None:
            self.media_id_white_list_shrink = m.get('MediaIdWhiteList')

        if m.get('MediaIndustry') is not None:
            self.media_industry = m.get('MediaIndustry')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OptimizationSwitch') is not None:
            self.optimization_switch = m.get('OptimizationSwitch')

        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('QuotaDay') is not None:
            self.quota_day = m.get('QuotaDay')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskBizType') is not None:
            self.task_biz_type = m.get('TaskBizType')

        if m.get('TaskRuleType') is not None:
            self.task_rule_type = m.get('TaskRuleType')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

