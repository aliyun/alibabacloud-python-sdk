# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class DescribeDataAgentSkillDownloadResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDataAgentSkillDownloadResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response struct.
        self.data = data
        # The error code returned when a request exception occurs.
        self.error_code = error_code
        # The error message returned when the call fails.
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **true**: The request is successful.
        # - **false**: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDataAgentSkillDownloadResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDataAgentSkillDownloadResponseBodyData(DaraModel):
    def __init__(
        self,
        download_link: str = None,
        intranet_download_link: str = None,
        skill_id: str = None,
        skill_name: str = None,
    ):
        # The public download link.
        self.download_link = download_link
        # The internal network download link.
        self.intranet_download_link = intranet_download_link
        # The skill ID.
        self.skill_id = skill_id
        # The skill name.
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        return self

