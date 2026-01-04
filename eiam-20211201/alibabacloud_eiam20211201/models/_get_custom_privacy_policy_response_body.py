# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetCustomPrivacyPolicyResponseBody(DaraModel):
    def __init__(
        self,
        custom_privacy_policy: main_models.GetCustomPrivacyPolicyResponseBodyCustomPrivacyPolicy = None,
        request_id: str = None,
    ):
        self.custom_privacy_policy = custom_privacy_policy
        self.request_id = request_id

    def validate(self):
        if self.custom_privacy_policy:
            self.custom_privacy_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_privacy_policy is not None:
            result['CustomPrivacyPolicy'] = self.custom_privacy_policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPrivacyPolicy') is not None:
            temp_model = main_models.GetCustomPrivacyPolicyResponseBodyCustomPrivacyPolicy()
            self.custom_privacy_policy = temp_model.from_map(m.get('CustomPrivacyPolicy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCustomPrivacyPolicyResponseBodyCustomPrivacyPolicy(DaraModel):
    def __init__(
        self,
        custom_privacy_policy_contents: List[main_models.GetCustomPrivacyPolicyResponseBodyCustomPrivacyPolicyCustomPrivacyPolicyContents] = None,
        custom_privacy_policy_id: str = None,
        custom_privacy_policy_name: str = None,
        default_language_code: str = None,
        instance_id: str = None,
        status: str = None,
        user_consent_type: str = None,
    ):
        self.custom_privacy_policy_contents = custom_privacy_policy_contents
        self.custom_privacy_policy_id = custom_privacy_policy_id
        self.custom_privacy_policy_name = custom_privacy_policy_name
        self.default_language_code = default_language_code
        self.instance_id = instance_id
        self.status = status
        self.user_consent_type = user_consent_type

    def validate(self):
        if self.custom_privacy_policy_contents:
            for v1 in self.custom_privacy_policy_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomPrivacyPolicyContents'] = []
        if self.custom_privacy_policy_contents is not None:
            for k1 in self.custom_privacy_policy_contents:
                result['CustomPrivacyPolicyContents'].append(k1.to_map() if k1 else None)

        if self.custom_privacy_policy_id is not None:
            result['CustomPrivacyPolicyId'] = self.custom_privacy_policy_id

        if self.custom_privacy_policy_name is not None:
            result['CustomPrivacyPolicyName'] = self.custom_privacy_policy_name

        if self.default_language_code is not None:
            result['DefaultLanguageCode'] = self.default_language_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_consent_type is not None:
            result['UserConsentType'] = self.user_consent_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_privacy_policy_contents = []
        if m.get('CustomPrivacyPolicyContents') is not None:
            for k1 in m.get('CustomPrivacyPolicyContents'):
                temp_model = main_models.GetCustomPrivacyPolicyResponseBodyCustomPrivacyPolicyCustomPrivacyPolicyContents()
                self.custom_privacy_policy_contents.append(temp_model.from_map(k1))

        if m.get('CustomPrivacyPolicyId') is not None:
            self.custom_privacy_policy_id = m.get('CustomPrivacyPolicyId')

        if m.get('CustomPrivacyPolicyName') is not None:
            self.custom_privacy_policy_name = m.get('CustomPrivacyPolicyName')

        if m.get('DefaultLanguageCode') is not None:
            self.default_language_code = m.get('DefaultLanguageCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserConsentType') is not None:
            self.user_consent_type = m.get('UserConsentType')

        return self

class GetCustomPrivacyPolicyResponseBodyCustomPrivacyPolicyCustomPrivacyPolicyContents(DaraModel):
    def __init__(
        self,
        custom_privacy_policy_items: List[main_models.GetCustomPrivacyPolicyResponseBodyCustomPrivacyPolicyCustomPrivacyPolicyContentsCustomPrivacyPolicyItems] = None,
        custom_privacy_policy_tip: str = None,
        language_code: str = None,
    ):
        self.custom_privacy_policy_items = custom_privacy_policy_items
        self.custom_privacy_policy_tip = custom_privacy_policy_tip
        self.language_code = language_code

    def validate(self):
        if self.custom_privacy_policy_items:
            for v1 in self.custom_privacy_policy_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomPrivacyPolicyItems'] = []
        if self.custom_privacy_policy_items is not None:
            for k1 in self.custom_privacy_policy_items:
                result['CustomPrivacyPolicyItems'].append(k1.to_map() if k1 else None)

        if self.custom_privacy_policy_tip is not None:
            result['CustomPrivacyPolicyTip'] = self.custom_privacy_policy_tip

        if self.language_code is not None:
            result['LanguageCode'] = self.language_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_privacy_policy_items = []
        if m.get('CustomPrivacyPolicyItems') is not None:
            for k1 in m.get('CustomPrivacyPolicyItems'):
                temp_model = main_models.GetCustomPrivacyPolicyResponseBodyCustomPrivacyPolicyCustomPrivacyPolicyContentsCustomPrivacyPolicyItems()
                self.custom_privacy_policy_items.append(temp_model.from_map(k1))

        if m.get('CustomPrivacyPolicyTip') is not None:
            self.custom_privacy_policy_tip = m.get('CustomPrivacyPolicyTip')

        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')

        return self

class GetCustomPrivacyPolicyResponseBodyCustomPrivacyPolicyCustomPrivacyPolicyContentsCustomPrivacyPolicyItems(DaraModel):
    def __init__(
        self,
        custom_privacy_policy_item_name: str = None,
        custom_privacy_policy_item_url: str = None,
    ):
        self.custom_privacy_policy_item_name = custom_privacy_policy_item_name
        self.custom_privacy_policy_item_url = custom_privacy_policy_item_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_privacy_policy_item_name is not None:
            result['CustomPrivacyPolicyItemName'] = self.custom_privacy_policy_item_name

        if self.custom_privacy_policy_item_url is not None:
            result['CustomPrivacyPolicyItemUrl'] = self.custom_privacy_policy_item_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPrivacyPolicyItemName') is not None:
            self.custom_privacy_policy_item_name = m.get('CustomPrivacyPolicyItemName')

        if m.get('CustomPrivacyPolicyItemUrl') is not None:
            self.custom_privacy_policy_item_url = m.get('CustomPrivacyPolicyItemUrl')

        return self

