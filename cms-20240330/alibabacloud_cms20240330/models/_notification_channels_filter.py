# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class NotificationChannelsFilter(DaraModel):
    def __init__(
        self,
        contains_contacts: List[str] = None,
        contains_custom_webhooks: List[str] = None,
        contains_ding_webhooks: List[str] = None,
        contains_fs_webhooks: List[str] = None,
        contains_groups: List[str] = None,
        contains_slack_webhooks: List[str] = None,
        contains_wx_webhooks: List[str] = None,
    ):
        self.contains_contacts = contains_contacts
        self.contains_custom_webhooks = contains_custom_webhooks
        self.contains_ding_webhooks = contains_ding_webhooks
        self.contains_fs_webhooks = contains_fs_webhooks
        self.contains_groups = contains_groups
        self.contains_slack_webhooks = contains_slack_webhooks
        self.contains_wx_webhooks = contains_wx_webhooks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contains_contacts is not None:
            result['containsContacts'] = self.contains_contacts

        if self.contains_custom_webhooks is not None:
            result['containsCustomWebhooks'] = self.contains_custom_webhooks

        if self.contains_ding_webhooks is not None:
            result['containsDingWebhooks'] = self.contains_ding_webhooks

        if self.contains_fs_webhooks is not None:
            result['containsFsWebhooks'] = self.contains_fs_webhooks

        if self.contains_groups is not None:
            result['containsGroups'] = self.contains_groups

        if self.contains_slack_webhooks is not None:
            result['containsSlackWebhooks'] = self.contains_slack_webhooks

        if self.contains_wx_webhooks is not None:
            result['containsWxWebhooks'] = self.contains_wx_webhooks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containsContacts') is not None:
            self.contains_contacts = m.get('containsContacts')

        if m.get('containsCustomWebhooks') is not None:
            self.contains_custom_webhooks = m.get('containsCustomWebhooks')

        if m.get('containsDingWebhooks') is not None:
            self.contains_ding_webhooks = m.get('containsDingWebhooks')

        if m.get('containsFsWebhooks') is not None:
            self.contains_fs_webhooks = m.get('containsFsWebhooks')

        if m.get('containsGroups') is not None:
            self.contains_groups = m.get('containsGroups')

        if m.get('containsSlackWebhooks') is not None:
            self.contains_slack_webhooks = m.get('containsSlackWebhooks')

        if m.get('containsWxWebhooks') is not None:
            self.contains_wx_webhooks = m.get('containsWxWebhooks')

        return self

