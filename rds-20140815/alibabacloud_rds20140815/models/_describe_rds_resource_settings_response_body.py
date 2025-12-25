# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRdsResourceSettingsResponseBody(DaraModel):
    def __init__(
        self,
        rds_instance_resource_settings: main_models.DescribeRdsResourceSettingsResponseBodyRdsInstanceResourceSettings = None,
        request_id: str = None,
    ):
        # The details about notification settings for an instance.
        self.rds_instance_resource_settings = rds_instance_resource_settings
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.rds_instance_resource_settings:
            self.rds_instance_resource_settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rds_instance_resource_settings is not None:
            result['RdsInstanceResourceSettings'] = self.rds_instance_resource_settings.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RdsInstanceResourceSettings') is not None:
            temp_model = main_models.DescribeRdsResourceSettingsResponseBodyRdsInstanceResourceSettings()
            self.rds_instance_resource_settings = temp_model.from_map(m.get('RdsInstanceResourceSettings'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRdsResourceSettingsResponseBodyRdsInstanceResourceSettings(DaraModel):
    def __init__(
        self,
        rds_instance_resource_setting: List[main_models.DescribeRdsResourceSettingsResponseBodyRdsInstanceResourceSettingsRdsInstanceResourceSetting] = None,
    ):
        self.rds_instance_resource_setting = rds_instance_resource_setting

    def validate(self):
        if self.rds_instance_resource_setting:
            for v1 in self.rds_instance_resource_setting:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RdsInstanceResourceSetting'] = []
        if self.rds_instance_resource_setting is not None:
            for k1 in self.rds_instance_resource_setting:
                result['RdsInstanceResourceSetting'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rds_instance_resource_setting = []
        if m.get('RdsInstanceResourceSetting') is not None:
            for k1 in m.get('RdsInstanceResourceSetting'):
                temp_model = main_models.DescribeRdsResourceSettingsResponseBodyRdsInstanceResourceSettingsRdsInstanceResourceSetting()
                self.rds_instance_resource_setting.append(temp_model.from_map(k1))

        return self

class DescribeRdsResourceSettingsResponseBodyRdsInstanceResourceSettingsRdsInstanceResourceSetting(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        is_top: str = None,
        notice_bar_content: str = None,
        popped_up_button_text: str = None,
        popped_up_button_type: str = None,
        popped_up_button_url: str = None,
        popped_up_content: str = None,
        resource_niche: str = None,
        start_date: str = None,
    ):
        # The end date.
        self.end_date = end_date
        # Specifies whether to pin the notification at the top.
        # 
        # *   true
        # *   false
        self.is_top = is_top
        # The notification text.
        self.notice_bar_content = notice_bar_content
        # The text of the popup button.
        self.popped_up_button_text = popped_up_button_text
        # The type of the popup button.
        # 
        # *   BUY
        # *   RENEW
        # *   UPGRADE
        self.popped_up_button_type = popped_up_button_type
        # The link of the popup button.
        self.popped_up_button_url = popped_up_button_url
        # The text of the popup.
        self.popped_up_content = popped_up_content
        # The location of the notification.
        self.resource_niche = resource_niche
        # The effective date.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.is_top is not None:
            result['IsTop'] = self.is_top

        if self.notice_bar_content is not None:
            result['NoticeBarContent'] = self.notice_bar_content

        if self.popped_up_button_text is not None:
            result['PoppedUpButtonText'] = self.popped_up_button_text

        if self.popped_up_button_type is not None:
            result['PoppedUpButtonType'] = self.popped_up_button_type

        if self.popped_up_button_url is not None:
            result['PoppedUpButtonUrl'] = self.popped_up_button_url

        if self.popped_up_content is not None:
            result['PoppedUpContent'] = self.popped_up_content

        if self.resource_niche is not None:
            result['ResourceNiche'] = self.resource_niche

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('IsTop') is not None:
            self.is_top = m.get('IsTop')

        if m.get('NoticeBarContent') is not None:
            self.notice_bar_content = m.get('NoticeBarContent')

        if m.get('PoppedUpButtonText') is not None:
            self.popped_up_button_text = m.get('PoppedUpButtonText')

        if m.get('PoppedUpButtonType') is not None:
            self.popped_up_button_type = m.get('PoppedUpButtonType')

        if m.get('PoppedUpButtonUrl') is not None:
            self.popped_up_button_url = m.get('PoppedUpButtonUrl')

        if m.get('PoppedUpContent') is not None:
            self.popped_up_content = m.get('PoppedUpContent')

        if m.get('ResourceNiche') is not None:
            self.resource_niche = m.get('ResourceNiche')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

