# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class CreateApsWebhookRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        job_type: str = None,
        region_id: str = None,
        webhook: List[main_models.CreateApsWebhookRequestWebhook] = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The type of the task. Valid value: Task type. SLS or OSS Export Task: ResultExport.
        # 
        # This parameter is required.
        self.job_type = job_type
        # The ID of the region in which to create the dedicated block storage cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The array of webhooks.
        self.webhook = webhook

    def validate(self):
        if self.webhook:
            for v1 in self.webhook:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Webhook'] = []
        if self.webhook is not None:
            for k1 in self.webhook:
                result['Webhook'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.webhook = []
        if m.get('Webhook') is not None:
            for k1 in m.get('Webhook'):
                temp_model = main_models.CreateApsWebhookRequestWebhook()
                self.webhook.append(temp_model.from_map(k1))

        return self

class CreateApsWebhookRequestWebhook(DaraModel):
    def __init__(
        self,
        key: str = None,
        name: str = None,
        url: str = None,
        webhook_type: str = None,
    ):
        # Signed key.
        self.key = key
        # The name of the webhook.
        self.name = name
        # The request path.
        # 
        # This parameter is required.
        self.url = url
        # The notification method. Valid values: dingtalk. lark.
        # 
        # This parameter is required.
        self.webhook_type = webhook_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        if self.url is not None:
            result['Url'] = self.url

        if self.webhook_type is not None:
            result['WebhookType'] = self.webhook_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WebhookType') is not None:
            self.webhook_type = m.get('WebhookType')

        return self

