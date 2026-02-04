# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDtsEtlJobVersionInfoResponseBody(DaraModel):
    def __init__(
        self,
        dts_etl_job_version_infos: List[main_models.DescribeDtsEtlJobVersionInfoResponseBodyDtsEtlJobVersionInfos] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: bool = None,
        total_record_count: int = None,
    ):
        # The details of ETL tasks.
        self.dts_etl_job_version_infos = dts_etl_job_version_infos
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message.
        self.dynamic_message = dynamic_message
        # The error code. This example indicates that the specified ETL task ID is invalid.
        self.err_code = err_code
        # The error message. This example indicates that the specified ETL task ID does not exist. In this case, the ETL task may have been deleted.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The page number of the returned page. Default value: 1.
        self.page_number = page_number
        # The number of records returned on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. If the call failed, false is returned.
        self.success = success
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.dts_etl_job_version_infos:
            for v1 in self.dts_etl_job_version_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DtsEtlJobVersionInfos'] = []
        if self.dts_etl_job_version_infos is not None:
            for k1 in self.dts_etl_job_version_infos:
                result['DtsEtlJobVersionInfos'].append(k1.to_map() if k1 else None)

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dts_etl_job_version_infos = []
        if m.get('DtsEtlJobVersionInfos') is not None:
            for k1 in m.get('DtsEtlJobVersionInfos'):
                temp_model = main_models.DescribeDtsEtlJobVersionInfoResponseBodyDtsEtlJobVersionInfos()
                self.dts_etl_job_version_infos.append(temp_model.from_map(k1))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDtsEtlJobVersionInfoResponseBodyDtsEtlJobVersionInfos(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator: str = None,
        creator_name: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        modify_time: str = None,
        safe_checkpoint: str = None,
        status: str = None,
        version: int = None,
    ):
        # The time when the ETL task was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The ID of the creator.
        self.creator = creator
        # The username of the creator.
        self.creator_name = creator_name
        # The ID of the DTS instance.
        self.dts_instance_id = dts_instance_id
        # The ID of the ETL task.
        self.dts_job_id = dts_job_id
        # The name of the ETL task.
        self.dts_job_name = dts_job_name
        # The time when the ETL task was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.modify_time = modify_time
        # The safe checkpoint of the ETL task.
        self.safe_checkpoint = safe_checkpoint
        # The log level. Valid values: ERROR, WARN, INFO, and DEBUG.
        self.status = status
        # The version number of the ETL task.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.safe_checkpoint is not None:
            result['SafeCheckpoint'] = self.safe_checkpoint

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('SafeCheckpoint') is not None:
            self.safe_checkpoint = m.get('SafeCheckpoint')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

