# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateScreenshotRequest(DaraModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        oss_bucket_name: str = None,
        screenshot_id: str = None,
        skip_check_policy_config: str = None,
    ):
        # The list of instance IDs. Batch screenshots are supported.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # The custom OSS bucket. The bucket name must start with the cloudphone-saved-bucket- prefix. The cloud phone instance and the OSS bucket must be in the same region. If you leave this parameter empty, a default bucket named cloudphone-saved-bucket-{RegionOfCloudPhone}-{AliUid} is created.
        self.oss_bucket_name = oss_bucket_name
        # The screenshot ID. The generated screenshot is named "ScreenshotId_AndroidInstanceId.png."
        # 
        # >Notice: 
        # 
        # The ScreenshotId must be 2 to 128 characters long, beginning with a letter, but cannot start with http\\:// or https\\://. Allowed characters include letters, digits, underscores (_), and hyphens (-).
        self.screenshot_id = screenshot_id
        # Specifies whether to skip the screenshot policy check. The default value is false.
        self.skip_check_policy_config = skip_check_policy_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.screenshot_id is not None:
            result['ScreenshotId'] = self.screenshot_id

        if self.skip_check_policy_config is not None:
            result['SkipCheckPolicyConfig'] = self.skip_check_policy_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('ScreenshotId') is not None:
            self.screenshot_id = m.get('ScreenshotId')

        if m.get('SkipCheckPolicyConfig') is not None:
            self.skip_check_policy_config = m.get('SkipCheckPolicyConfig')

        return self

