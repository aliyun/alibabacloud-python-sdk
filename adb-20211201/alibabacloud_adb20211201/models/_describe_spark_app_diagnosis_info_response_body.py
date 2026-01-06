# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeSparkAppDiagnosisInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        app_id: str = None,
        cpu_utilization: float = None,
        diagnosis_info_list: List[main_models.Adb4MysqlSparkDiagnosisInfo] = None,
        duration_in_millis: int = None,
        jvmgc_cost_in_millis: int = None,
        peak_memory_in_byte: int = None,
        request_id: str = None,
        shuffle_read_in_byte: int = None,
        shuffle_write_in_byte: int = None,
        spill_in_byte: int = None,
        started_time: int = None,
        state: str = None,
    ):
        # The information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The application ID.
        # 
        # >  You can call the [ListSparkApps](https://help.aliyun.com/document_detail/455888.html) operation to query all application IDs.
        self.app_id = app_id
        # The CPU utilization. Unit: %.
        self.cpu_utilization = cpu_utilization
        # The queried diagnostic information.
        self.diagnosis_info_list = diagnosis_info_list
        # The execution duration of the application. Unit: milliseconds.
        self.duration_in_millis = duration_in_millis
        # The amount of time consumed by the Java virtual machine to perform garbage collection operations. Unit: milliseconds.
        self.jvmgc_cost_in_millis = jvmgc_cost_in_millis
        # The peak memory usage. Unit: bytes.
        self.peak_memory_in_byte = peak_memory_in_byte
        # The request ID.
        self.request_id = request_id
        # The amount of data used for shuffle reads. Unit: bytes.
        self.shuffle_read_in_byte = shuffle_read_in_byte
        # The amount of data used for shuffle writes. Unit: bytes.
        self.shuffle_write_in_byte = shuffle_write_in_byte
        # The amount of data spilled to disks when the memory is insufficient. Unit: bytes.
        self.spill_in_byte = spill_in_byte
        # The time when the application started to be executed.
        self.started_time = started_time
        # The status of the asynchronous import or export job. Valid values:
        # 
        # *   **RUNNING**
        # *   **FINISHED**
        # *   **FAILED**
        self.state = state

    def validate(self):
        if self.diagnosis_info_list:
            for v1 in self.diagnosis_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cpu_utilization is not None:
            result['CpuUtilization'] = self.cpu_utilization

        result['DiagnosisInfoList'] = []
        if self.diagnosis_info_list is not None:
            for k1 in self.diagnosis_info_list:
                result['DiagnosisInfoList'].append(k1.to_map() if k1 else None)

        if self.duration_in_millis is not None:
            result['DurationInMillis'] = self.duration_in_millis

        if self.jvmgc_cost_in_millis is not None:
            result['JVMGcCostInMillis'] = self.jvmgc_cost_in_millis

        if self.peak_memory_in_byte is not None:
            result['PeakMemoryInByte'] = self.peak_memory_in_byte

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.shuffle_read_in_byte is not None:
            result['ShuffleReadInByte'] = self.shuffle_read_in_byte

        if self.shuffle_write_in_byte is not None:
            result['ShuffleWriteInByte'] = self.shuffle_write_in_byte

        if self.spill_in_byte is not None:
            result['SpillInByte'] = self.spill_in_byte

        if self.started_time is not None:
            result['StartedTime'] = self.started_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CpuUtilization') is not None:
            self.cpu_utilization = m.get('CpuUtilization')

        self.diagnosis_info_list = []
        if m.get('DiagnosisInfoList') is not None:
            for k1 in m.get('DiagnosisInfoList'):
                temp_model = main_models.Adb4MysqlSparkDiagnosisInfo()
                self.diagnosis_info_list.append(temp_model.from_map(k1))

        if m.get('DurationInMillis') is not None:
            self.duration_in_millis = m.get('DurationInMillis')

        if m.get('JVMGcCostInMillis') is not None:
            self.jvmgc_cost_in_millis = m.get('JVMGcCostInMillis')

        if m.get('PeakMemoryInByte') is not None:
            self.peak_memory_in_byte = m.get('PeakMemoryInByte')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShuffleReadInByte') is not None:
            self.shuffle_read_in_byte = m.get('ShuffleReadInByte')

        if m.get('ShuffleWriteInByte') is not None:
            self.shuffle_write_in_byte = m.get('ShuffleWriteInByte')

        if m.get('SpillInByte') is not None:
            self.spill_in_byte = m.get('SpillInByte')

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

