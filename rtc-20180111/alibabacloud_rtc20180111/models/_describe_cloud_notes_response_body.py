# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudNotesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeCloudNotesResponseBodyItems] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
    ):
        self.items = items
        self.page_no = page_no
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_cnt = total_cnt

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeCloudNotesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')

        return self

class DescribeCloudNotesResponseBodyItems(DaraModel):
    def __init__(
        self,
        auto_chapters_file_path: str = None,
        bucket: str = None,
        channel_id: str = None,
        custom_prompt_file_path: str = None,
        meeting_assistance_file_path: str = None,
        region: int = None,
        service_inspection_file_path: str = None,
        start_ts: int = None,
        summarization_file_path: str = None,
        task_id: str = None,
        text_polish_file_path: str = None,
        transcription_file_path: str = None,
        vendor: int = None,
    ):
        self.auto_chapters_file_path = auto_chapters_file_path
        self.bucket = bucket
        self.channel_id = channel_id
        self.custom_prompt_file_path = custom_prompt_file_path
        self.meeting_assistance_file_path = meeting_assistance_file_path
        self.region = region
        self.service_inspection_file_path = service_inspection_file_path
        self.start_ts = start_ts
        self.summarization_file_path = summarization_file_path
        self.task_id = task_id
        self.text_polish_file_path = text_polish_file_path
        self.transcription_file_path = transcription_file_path
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_chapters_file_path is not None:
            result['AutoChaptersFilePath'] = self.auto_chapters_file_path

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.custom_prompt_file_path is not None:
            result['CustomPromptFilePath'] = self.custom_prompt_file_path

        if self.meeting_assistance_file_path is not None:
            result['MeetingAssistanceFilePath'] = self.meeting_assistance_file_path

        if self.region is not None:
            result['Region'] = self.region

        if self.service_inspection_file_path is not None:
            result['ServiceInspectionFilePath'] = self.service_inspection_file_path

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        if self.summarization_file_path is not None:
            result['SummarizationFilePath'] = self.summarization_file_path

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.text_polish_file_path is not None:
            result['TextPolishFilePath'] = self.text_polish_file_path

        if self.transcription_file_path is not None:
            result['TranscriptionFilePath'] = self.transcription_file_path

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoChaptersFilePath') is not None:
            self.auto_chapters_file_path = m.get('AutoChaptersFilePath')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CustomPromptFilePath') is not None:
            self.custom_prompt_file_path = m.get('CustomPromptFilePath')

        if m.get('MeetingAssistanceFilePath') is not None:
            self.meeting_assistance_file_path = m.get('MeetingAssistanceFilePath')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ServiceInspectionFilePath') is not None:
            self.service_inspection_file_path = m.get('ServiceInspectionFilePath')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        if m.get('SummarizationFilePath') is not None:
            self.summarization_file_path = m.get('SummarizationFilePath')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TextPolishFilePath') is not None:
            self.text_polish_file_path = m.get('TextPolishFilePath')

        if m.get('TranscriptionFilePath') is not None:
            self.transcription_file_path = m.get('TranscriptionFilePath')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

