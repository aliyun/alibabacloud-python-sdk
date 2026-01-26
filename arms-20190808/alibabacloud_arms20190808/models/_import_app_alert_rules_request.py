# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ImportAppAlertRulesRequest(DaraModel):
    def __init__(
        self,
        contact_group_ids: str = None,
        is_auto_start: bool = None,
        pids: str = None,
        region_id: str = None,
        tags: List[main_models.ImportAppAlertRulesRequestTags] = None,
        templage_alert_config: str = None,
        template_alert_id: str = None,
    ):
        # The IDs of the alert contact groups. The value must be a JSON array.
        self.contact_group_ids = contact_group_ids
        # Specifies whether to enable the alert rule after it is created. Default value: `false`.
        # 
        # *   `true`: enables the alert rule.
        # *   `false`: disables the alert rule.
        self.is_auto_start = is_auto_start
        # The process identifiers (PIDs) of the applications associated with the alert rule. The value must be a JSON array. For more information about how to obtain the PID, see [Obtain the PID of an application](~~186100#section-bkl-3j6-ezg~~).
        # 
        # This parameter is required.
        self.pids = pids
        # The ID of the region where the associated applications reside.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of tags.
        self.tags = tags
        # The configurations of the alert template based on which you want to create an alert rule. The value must be a JSON string. You must set at least one of the **TemplateAlertId** and **TemplageAlertConfig** parameters. If you set both parameters, the **TemplateAlertId** parameter prevails. For more information about the TemplageAlertConfig parameter, see the following **additional information about the TemplageAlertConfig parameter**.
        self.templage_alert_config = templage_alert_config
        # The ID of the alert template. You must set at least one of the **TemplateAlertId** and **TemplageAlertConfig** parameters. If you set both parameters, the **TemplateAlertId** parameter prevails.
        self.template_alert_id = template_alert_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids

        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start

        if self.pids is not None:
            result['Pids'] = self.pids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config

        if self.template_alert_id is not None:
            result['TemplateAlertId'] = self.template_alert_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')

        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')

        if m.get('Pids') is not None:
            self.pids = m.get('Pids')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ImportAppAlertRulesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')

        if m.get('TemplateAlertId') is not None:
            self.template_alert_id = m.get('TemplateAlertId')

        return self

class ImportAppAlertRulesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

