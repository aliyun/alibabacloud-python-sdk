# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DisposalContent(DaraModel):
    def __init__(
        self,
        alert_content: str = None,
        alert_content_en: str = None,
        alert_interval_seconds: int = None,
        alert_title: str = None,
        alert_title_en: str = None,
        nac_demotion_policy_ids: List[str] = None,
        notice_content: str = None,
        notice_content_en: str = None,
        notify_actions: List[str] = None,
        prohibit_actions: List[str] = None,
        prohibit_software_ids: List[str] = None,
    ):
        self.alert_content = alert_content
        self.alert_content_en = alert_content_en
        self.alert_interval_seconds = alert_interval_seconds
        self.alert_title = alert_title
        self.alert_title_en = alert_title_en
        self.nac_demotion_policy_ids = nac_demotion_policy_ids
        self.notice_content = notice_content
        self.notice_content_en = notice_content_en
        # This parameter is required.
        self.notify_actions = notify_actions
        self.prohibit_actions = prohibit_actions
        self.prohibit_software_ids = prohibit_software_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_content is not None:
            result['AlertContent'] = self.alert_content

        if self.alert_content_en is not None:
            result['AlertContentEn'] = self.alert_content_en

        if self.alert_interval_seconds is not None:
            result['AlertIntervalSeconds'] = self.alert_interval_seconds

        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title

        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en

        if self.nac_demotion_policy_ids is not None:
            result['NacDemotionPolicyIds'] = self.nac_demotion_policy_ids

        if self.notice_content is not None:
            result['NoticeContent'] = self.notice_content

        if self.notice_content_en is not None:
            result['NoticeContentEn'] = self.notice_content_en

        if self.notify_actions is not None:
            result['NotifyActions'] = self.notify_actions

        if self.prohibit_actions is not None:
            result['ProhibitActions'] = self.prohibit_actions

        if self.prohibit_software_ids is not None:
            result['ProhibitSoftwareIds'] = self.prohibit_software_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertContent') is not None:
            self.alert_content = m.get('AlertContent')

        if m.get('AlertContentEn') is not None:
            self.alert_content_en = m.get('AlertContentEn')

        if m.get('AlertIntervalSeconds') is not None:
            self.alert_interval_seconds = m.get('AlertIntervalSeconds')

        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')

        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')

        if m.get('NacDemotionPolicyIds') is not None:
            self.nac_demotion_policy_ids = m.get('NacDemotionPolicyIds')

        if m.get('NoticeContent') is not None:
            self.notice_content = m.get('NoticeContent')

        if m.get('NoticeContentEn') is not None:
            self.notice_content_en = m.get('NoticeContentEn')

        if m.get('NotifyActions') is not None:
            self.notify_actions = m.get('NotifyActions')

        if m.get('ProhibitActions') is not None:
            self.prohibit_actions = m.get('ProhibitActions')

        if m.get('ProhibitSoftwareIds') is not None:
            self.prohibit_software_ids = m.get('ProhibitSoftwareIds')

        return self

