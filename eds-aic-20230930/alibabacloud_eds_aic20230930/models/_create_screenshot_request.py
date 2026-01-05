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
        # The IDs of the cloud phone instances. You can create multiple snapshots simultaneously.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # The name of the OSS bucket. The name must start with "cloudphone-saved-bucket-". The OSS bucket and the cloud phone instance must be in the same region. If you leave this parameter empty, the system will create a default OSS bucket named “cloudphone-saved-bucket-{Region of the cloud phone instance}-{AliUid}.”
        self.oss_bucket_name = oss_bucket_name
        self.screenshot_id = screenshot_id
        # Specifies whether to bypass the snapshot policy control. Default value: false.
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

