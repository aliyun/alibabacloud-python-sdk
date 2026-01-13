# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class JobDriver(DaraModel):
    def __init__(
        self,
        spark_submit: main_models.JobDriverSparkSubmit = None,
    ):
        self.spark_submit = spark_submit

    def validate(self):
        if self.spark_submit:
            self.spark_submit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.spark_submit is not None:
            result['sparkSubmit'] = self.spark_submit.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sparkSubmit') is not None:
            temp_model = main_models.JobDriverSparkSubmit()
            self.spark_submit = temp_model.from_map(m.get('sparkSubmit'))

        return self

class JobDriverSparkSubmit(DaraModel):
    def __init__(
        self,
        entry_point: str = None,
        entry_point_arguments: List[str] = None,
        spark_submit_parameters: str = None,
    ):
        self.entry_point = entry_point
        self.entry_point_arguments = entry_point_arguments
        self.spark_submit_parameters = spark_submit_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entry_point is not None:
            result['entryPoint'] = self.entry_point

        if self.entry_point_arguments is not None:
            result['entryPointArguments'] = self.entry_point_arguments

        if self.spark_submit_parameters is not None:
            result['sparkSubmitParameters'] = self.spark_submit_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entryPoint') is not None:
            self.entry_point = m.get('entryPoint')

        if m.get('entryPointArguments') is not None:
            self.entry_point_arguments = m.get('entryPointArguments')

        if m.get('sparkSubmitParameters') is not None:
            self.spark_submit_parameters = m.get('sparkSubmitParameters')

        return self

