# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetCorpTasksResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetCorpTasksResponseBodyData] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.data = data
        self.page_number = page_number
        self.request_id = request_id
        self.total_count = total_count
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetCorpTasksResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetCorpTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        active_time_gmt: str = None,
        actual_actioner_id: str = None,
        app_type: str = None,
        create_time_gmt: str = None,
        finish_time_gmt: str = None,
        originator_email: str = None,
        originator_id: str = None,
        originator_name: str = None,
        originator_name_in_english: str = None,
        originator_nick_name: str = None,
        originator_nick_name_en: str = None,
        originator_nick_name_in_english: str = None,
        originator_photo: str = None,
        out_result: str = None,
        out_result_name: str = None,
        process_instance_id: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        title: str = None,
        title_in_english: str = None,
    ):
        self.active_time_gmt = active_time_gmt
        self.actual_actioner_id = actual_actioner_id
        self.app_type = app_type
        self.create_time_gmt = create_time_gmt
        self.finish_time_gmt = finish_time_gmt
        self.originator_email = originator_email
        self.originator_id = originator_id
        self.originator_name = originator_name
        self.originator_name_in_english = originator_name_in_english
        self.originator_nick_name = originator_nick_name
        self.originator_nick_name_en = originator_nick_name_en
        self.originator_nick_name_in_english = originator_nick_name_in_english
        self.originator_photo = originator_photo
        self.out_result = out_result
        self.out_result_name = out_result_name
        self.process_instance_id = process_instance_id
        self.status = status
        self.task_id = task_id
        self.task_type = task_type
        self.title = title
        self.title_in_english = title_in_english

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_time_gmt is not None:
            result['ActiveTimeGMT'] = self.active_time_gmt

        if self.actual_actioner_id is not None:
            result['ActualActionerId'] = self.actual_actioner_id

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.create_time_gmt is not None:
            result['CreateTimeGMT'] = self.create_time_gmt

        if self.finish_time_gmt is not None:
            result['FinishTimeGMT'] = self.finish_time_gmt

        if self.originator_email is not None:
            result['OriginatorEmail'] = self.originator_email

        if self.originator_id is not None:
            result['OriginatorId'] = self.originator_id

        if self.originator_name is not None:
            result['OriginatorName'] = self.originator_name

        if self.originator_name_in_english is not None:
            result['OriginatorNameInEnglish'] = self.originator_name_in_english

        if self.originator_nick_name is not None:
            result['OriginatorNickName'] = self.originator_nick_name

        if self.originator_nick_name_en is not None:
            result['OriginatorNickNameEn'] = self.originator_nick_name_en

        if self.originator_nick_name_in_english is not None:
            result['OriginatorNickNameInEnglish'] = self.originator_nick_name_in_english

        if self.originator_photo is not None:
            result['OriginatorPhoto'] = self.originator_photo

        if self.out_result is not None:
            result['OutResult'] = self.out_result

        if self.out_result_name is not None:
            result['OutResultName'] = self.out_result_name

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.title is not None:
            result['Title'] = self.title

        if self.title_in_english is not None:
            result['TitleInEnglish'] = self.title_in_english

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTimeGMT') is not None:
            self.active_time_gmt = m.get('ActiveTimeGMT')

        if m.get('ActualActionerId') is not None:
            self.actual_actioner_id = m.get('ActualActionerId')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CreateTimeGMT') is not None:
            self.create_time_gmt = m.get('CreateTimeGMT')

        if m.get('FinishTimeGMT') is not None:
            self.finish_time_gmt = m.get('FinishTimeGMT')

        if m.get('OriginatorEmail') is not None:
            self.originator_email = m.get('OriginatorEmail')

        if m.get('OriginatorId') is not None:
            self.originator_id = m.get('OriginatorId')

        if m.get('OriginatorName') is not None:
            self.originator_name = m.get('OriginatorName')

        if m.get('OriginatorNameInEnglish') is not None:
            self.originator_name_in_english = m.get('OriginatorNameInEnglish')

        if m.get('OriginatorNickName') is not None:
            self.originator_nick_name = m.get('OriginatorNickName')

        if m.get('OriginatorNickNameEn') is not None:
            self.originator_nick_name_en = m.get('OriginatorNickNameEn')

        if m.get('OriginatorNickNameInEnglish') is not None:
            self.originator_nick_name_in_english = m.get('OriginatorNickNameInEnglish')

        if m.get('OriginatorPhoto') is not None:
            self.originator_photo = m.get('OriginatorPhoto')

        if m.get('OutResult') is not None:
            self.out_result = m.get('OutResult')

        if m.get('OutResultName') is not None:
            self.out_result_name = m.get('OutResultName')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TitleInEnglish') is not None:
            self.title_in_english = m.get('TitleInEnglish')

        return self

