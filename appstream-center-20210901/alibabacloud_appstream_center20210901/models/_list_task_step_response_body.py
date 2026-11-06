# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListTaskStepResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        data: List[main_models.ListTaskStepResponseBodyData] = None,
        request_id: str = None,
    ):
        # The total number of records returned in the list.
        self.count = count
        # The list of step definitions for the selected task type.
        self.data = data
        # The unique identifier of the request. You can provide this value for troubleshooting.
        self.request_id = request_id

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
        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListTaskStepResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTaskStepResponseBodyData(DaraModel):
    def __init__(
        self,
        action: str = None,
        category: str = None,
        category_en: str = None,
        index: int = None,
        name: str = None,
    ):
        # The interaction method of the step. Valid values:
        # - **prompt**: Displays step prompts.
        # - **connection**: Provides connection operations to enter the build or validation environment.
        # - **prompt_connection**: Provides both prompts and connection operations.
        self.action = action
        # The Chinese name of the phase to which the step belongs, such as build environment preparation or test validation.
        self.category = category
        # The English name of the phase to which the step belongs. This field is returned for image creation steps, but may not be returned for application adaptation steps.
        self.category_en = category_en
        # The numeric index of the step definition, which is used to identify the step and its sequence. Do not treat this value as a completion percentage.
        self.index = index
        # The name identifier of the step, which is used to match the step records returned by GetTask.
        # 
        # Steps when Type is set to IMAGE:
        # 
        # - **INIT**: Initializes the task.
        # - **CREATE_BUILDER_ENV**: Creates the build environment.
        # - **DEPLOY_BUILDER_ENV**: Deploys the build environment.
        # - **INIT_BUILDER**: Initializes the build tool.
        # - **DOWNLOAD_APP**: Downloads application resources.
        # - **START_BUILD**: Starts image creation.
        # - **COMPLETE_INSTALL**: Completes application installation and configuration.
        # - **CREATE_VALIDATE_ENV**: Creates the validation environment.
        # - **DEPLOY_VALIDATE_ENV**: Deploys the validation environment.
        # - **COMPLETE_VALIDATE**: Completes image validation.
        # - **ARCHIVE_DATA**: Archives image data.
        # - **CREATE_IMAGE**: Generates the image.
        # - **FINISH_ADAPT**: Ends the creation process.
        # 
        # Steps when Type is set to ADAPTOR:
        # 
        # - **INIT**: Initializes the task.
        # - **CREATE_BUILDER_ENV**: Creates the build environment.
        # - **DEPLOY_BUILDER_ENV**: Deploys the build environment.
        # - **INIT_BUILDER**: Initializes the build tool.
        # - **DOWNLOAD_APP**: Downloads application resources.
        # - **START_VHD**: Starts application recording.
        # - **BUILD_VHD**: Generates the application VHD.
        # - **UPLOAD_VHD**: Uploads the application VHD.
        # - **COMPLETE_BUILDER**: Completes application creation.
        # - **CREATE_VALIDATE_ENV**: Creates the validation environment.
        # - **DEPLOY_VALIDATE_ENV**: Deploys the validation environment.
        # - **COMPLETE_VALIDATE**: Completes application validation.
        # - **CREATE_IMAGE**: Generates the application image.
        # - **FINISH_ADAPT**: Ends the application adaptation process.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.category is not None:
            result['Category'] = self.category

        if self.category_en is not None:
            result['CategoryEn'] = self.category_en

        if self.index is not None:
            result['Index'] = self.index

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CategoryEn') is not None:
            self.category_en = m.get('CategoryEn')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

