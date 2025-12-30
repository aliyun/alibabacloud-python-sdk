# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryMediaCensorJobListResponseBody(DaraModel):
    def __init__(
        self,
        media_censor_job_list: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobList = None,
        next_page_token: str = None,
        non_exist_ids: main_models.QueryMediaCensorJobListResponseBodyNonExistIds = None,
        request_id: str = None,
    ):
        # The queried content moderation jobs.
        self.media_censor_job_list = media_censor_job_list
        # A pagination token. It can be used in the next request to retrieve a new page of results. The value is 32-character UUID. If the returned query results cannot be displayed within one page, this parameter is returned. The value of this parameter is updated for each query.
        self.next_page_token = next_page_token
        # The IDs of the jobs that do not exist. This parameter is not returned if all the specified jobs are found.
        self.non_exist_ids = non_exist_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_censor_job_list:
            self.media_censor_job_list.validate()
        if self.non_exist_ids:
            self.non_exist_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_censor_job_list is not None:
            result['MediaCensorJobList'] = self.media_censor_job_list.to_map()

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.non_exist_ids is not None:
            result['NonExistIds'] = self.non_exist_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaCensorJobList') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobList()
            self.media_censor_job_list = temp_model.from_map(m.get('MediaCensorJobList'))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('NonExistIds') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyNonExistIds()
            self.non_exist_ids = temp_model.from_map(m.get('NonExistIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryMediaCensorJobListResponseBodyNonExistIds(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobList(DaraModel):
    def __init__(
        self,
        media_censor_job: List[main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJob] = None,
    ):
        self.media_censor_job = media_censor_job

    def validate(self):
        if self.media_censor_job:
            for v1 in self.media_censor_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MediaCensorJob'] = []
        if self.media_censor_job is not None:
            for k1 in self.media_censor_job:
                result['MediaCensorJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media_censor_job = []
        if m.get('MediaCensorJob') is not None:
            for k1 in m.get('MediaCensorJob'):
                temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJob()
                self.media_censor_job.append(temp_model.from_map(k1))

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJob(DaraModel):
    def __init__(
        self,
        barrage_censor_result: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobBarrageCensorResult = None,
        code: str = None,
        cover_image_censor_results: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResults = None,
        creation_time: str = None,
        desc_censor_result: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobDescCensorResult = None,
        finish_time: str = None,
        input: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobInput = None,
        job_id: str = None,
        message: str = None,
        pipeline_id: str = None,
        state: str = None,
        suggestion: str = None,
        title_censor_result: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobTitleCensorResult = None,
        user_data: str = None,
        vensor_censor_result: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResult = None,
        video_censor_config: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVideoCensorConfig = None,
    ):
        # The moderation results of live comments.
        self.barrage_censor_result = barrage_censor_result
        # The error code returned if the job failed. This parameter is not returned if the job is successful.
        self.code = code
        # The moderation results of thumbnails.
        self.cover_image_censor_results = cover_image_censor_results
        # The time when the content moderation job was created.
        self.creation_time = creation_time
        # The moderation results of descriptions.
        self.desc_censor_result = desc_censor_result
        # The time when the content moderation job was complete.
        self.finish_time = finish_time
        # The information about the job input.
        self.input = input
        # The ID of the content moderation job.
        self.job_id = job_id
        # The error message returned if the job failed. This parameter is not returned if the job is successful.
        self.message = message
        # The ID of the MPS queue to which the job was submitted.
        self.pipeline_id = pipeline_id
        # The job state.
        self.state = state
        # The recommended subsequent operation. Valid values:
        # 
        # *   **pass**: The content passes the moderation.
        # *   **review**: The content needs to be manually reviewed.
        # *   **block**: The content needs to be blocked.
        self.suggestion = suggestion
        # The moderation results of titles.
        self.title_censor_result = title_censor_result
        # The user-defined data.
        self.user_data = user_data
        # The moderation results of videos.
        self.vensor_censor_result = vensor_censor_result
        # The video moderation configurations.
        self.video_censor_config = video_censor_config

    def validate(self):
        if self.barrage_censor_result:
            self.barrage_censor_result.validate()
        if self.cover_image_censor_results:
            self.cover_image_censor_results.validate()
        if self.desc_censor_result:
            self.desc_censor_result.validate()
        if self.input:
            self.input.validate()
        if self.title_censor_result:
            self.title_censor_result.validate()
        if self.vensor_censor_result:
            self.vensor_censor_result.validate()
        if self.video_censor_config:
            self.video_censor_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.barrage_censor_result is not None:
            result['BarrageCensorResult'] = self.barrage_censor_result.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.cover_image_censor_results is not None:
            result['CoverImageCensorResults'] = self.cover_image_censor_results.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.desc_censor_result is not None:
            result['DescCensorResult'] = self.desc_censor_result.to_map()

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.state is not None:
            result['State'] = self.state

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.title_censor_result is not None:
            result['TitleCensorResult'] = self.title_censor_result.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.vensor_censor_result is not None:
            result['VensorCensorResult'] = self.vensor_censor_result.to_map()

        if self.video_censor_config is not None:
            result['VideoCensorConfig'] = self.video_censor_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BarrageCensorResult') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobBarrageCensorResult()
            self.barrage_censor_result = temp_model.from_map(m.get('BarrageCensorResult'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CoverImageCensorResults') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResults()
            self.cover_image_censor_results = temp_model.from_map(m.get('CoverImageCensorResults'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DescCensorResult') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobDescCensorResult()
            self.desc_censor_result = temp_model.from_map(m.get('DescCensorResult'))

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Input') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('TitleCensorResult') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobTitleCensorResult()
            self.title_censor_result = temp_model.from_map(m.get('TitleCensorResult'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VensorCensorResult') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResult()
            self.vensor_censor_result = temp_model.from_map(m.get('VensorCensorResult'))

        if m.get('VideoCensorConfig') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVideoCensorConfig()
            self.video_censor_config = temp_model.from_map(m.get('VideoCensorConfig'))

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVideoCensorConfig(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        output_file: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVideoCensorConfigOutputFile = None,
        video_censor: str = None,
    ):
        # The moderation template. Default value: common. The default value indicates that the default template is used.
        # 
        # >  If the moderation template is not specified, the default value common is returned. If a custom moderation template that is created by submitting a ticket is specified, the UID of the template is returned.
        self.biz_type = biz_type
        # The information about output snapshots.
        self.output_file = output_file
        # Indicates whether the video content needs to be moderated. Default value: **true**. Valid values:
        # 
        # *   **true**: The video content needs to be moderated.
        # *   **false**: The video content does not need to be moderated.
        self.video_censor = video_censor

    def validate(self):
        if self.output_file:
            self.output_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.output_file is not None:
            result['OutputFile'] = self.output_file.to_map()

        if self.video_censor is not None:
            result['VideoCensor'] = self.video_censor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('OutputFile') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVideoCensorConfigOutputFile()
            self.output_file = temp_model.from_map(m.get('OutputFile'))

        if m.get('VideoCensor') is not None:
            self.video_censor = m.get('VideoCensor')

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVideoCensorConfigOutputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
    ):
        # The OSS bucket in which the output snapshot is stored.
        self.bucket = bucket
        # The ID of the region in which the output snapshot resides.
        self.location = location
        # The OSS object that is generated as the output snapshot.
        # 
        # >  In the example, {Count} is a placeholder. The OSS objects that are generated as output snapshots are named `output00001-****.jpg, output00002-****.jpg`, and so on.
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResult(DaraModel):
    def __init__(
        self,
        censor_results: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultCensorResults = None,
        next_page_token: str = None,
        video_timelines: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelines = None,
    ):
        # A collection of moderation results. The information includes the summary about various scenarios such as pornographic content moderation and terrorist content moderation.
        self.censor_results = censor_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_page_token = next_page_token
        # The moderation results that are sorted in ascending order by time.
        self.video_timelines = video_timelines

    def validate(self):
        if self.censor_results:
            self.censor_results.validate()
        if self.video_timelines:
            self.video_timelines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.censor_results is not None:
            result['CensorResults'] = self.censor_results.to_map()

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.video_timelines is not None:
            result['VideoTimelines'] = self.video_timelines.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CensorResults') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultCensorResults()
            self.censor_results = temp_model.from_map(m.get('CensorResults'))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('VideoTimelines') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelines()
            self.video_timelines = temp_model.from_map(m.get('VideoTimelines'))

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelines(DaraModel):
    def __init__(
        self,
        video_timeline: List[main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelinesVideoTimeline] = None,
    ):
        self.video_timeline = video_timeline

    def validate(self):
        if self.video_timeline:
            for v1 in self.video_timeline:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoTimeline'] = []
        if self.video_timeline is not None:
            for k1 in self.video_timeline:
                result['VideoTimeline'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_timeline = []
        if m.get('VideoTimeline') is not None:
            for k1 in m.get('VideoTimeline'):
                temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelinesVideoTimeline()
                self.video_timeline.append(temp_model.from_map(k1))

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelinesVideoTimeline(DaraModel):
    def __init__(
        self,
        censor_results: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelinesVideoTimelineCensorResults = None,
        object: str = None,
        timestamp: str = None,
    ):
        # The moderation results that include information such as labels and scores.
        self.censor_results = censor_results
        # The OSS object that is generated as the output snapshot.
        # 
        # >  In the example, {Count} is a placeholder. The OSS objects that are generated as output snapshots are named `output00001-****.jpg`, `output00002-****.jpg`, and so on.
        self.object = object
        # The position in the video. Format: `hh:mm:ss[.SSS]`.
        self.timestamp = timestamp

    def validate(self):
        if self.censor_results:
            self.censor_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.censor_results is not None:
            result['CensorResults'] = self.censor_results.to_map()

        if self.object is not None:
            result['Object'] = self.object

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CensorResults') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelinesVideoTimelineCensorResults()
            self.censor_results = temp_model.from_map(m.get('CensorResults'))

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelinesVideoTimelineCensorResults(DaraModel):
    def __init__(
        self,
        censor_result: List[main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelinesVideoTimelineCensorResultsCensorResult] = None,
    ):
        self.censor_result = censor_result

    def validate(self):
        if self.censor_result:
            for v1 in self.censor_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CensorResult'] = []
        if self.censor_result is not None:
            for k1 in self.censor_result:
                result['CensorResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.censor_result = []
        if m.get('CensorResult') is not None:
            for k1 in m.get('CensorResult'):
                temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelinesVideoTimelineCensorResultsCensorResult()
                self.censor_result.append(temp_model.from_map(k1))

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultVideoTimelinesVideoTimelineCensorResultsCensorResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        rate: str = None,
        scene: str = None,
        suggestion: str = None,
    ):
        # The label of the moderation result. Separate multiple labels with commas (,).
        # 
        # *   Valid values in the pornographic content moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **sexy**: sexy content.
        #     *   **porn**: pornographic content.
        # 
        # *   Valid values in the terrorist content moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **bloody**: bloody content.
        #     *   **explosion**: explosion and smoke.
        #     *   **outfit**: special costume.
        #     *   **logo**: special logo.
        #     *   **weapon**: weapon.
        #     *   **politics**: political content.
        #     *   **violence**: violence.
        #     *   **crowd**: crowd.
        #     *   **parade**: parade.
        #     *   **carcrash**: car accident.
        #     *   **flag**: flag.
        #     *   **location**: landmark.
        #     *   **others**: other content.
        # 
        # *   Valid values in the ad moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **ad**: other ads.
        #     *   **politics**: political content in text.
        #     *   **porn**: pornographic content in text.
        #     *   **abuse**: abuse in text.
        #     *   **terrorism**: terrorist content in text.
        #     *   **contraband**: prohibited content in text.
        #     *   **spam**: spam in text.
        #     *   **npx**: illegal ad.
        #     *   **qrcode**: QR code.
        #     *   **programCode**: mini program code.
        # 
        # *   Valid values in the undesirable scene moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **meaningless**: meaningless content, such as a black or white screen.
        #     *   **PIP**: picture-in-picture.
        #     *   **smoking**: smoking.
        #     *   **drivelive**: live streaming in a running vehicle.
        # 
        # *   Valid values in the logo moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **TV**: controlled logo.
        #     *   **trademark**: trademark.
        self.label = label
        # The score. Valid values: 0 to 100.
        self.rate = rate
        # The moderation scenario. Valid values:
        # 
        # *   **porn**: pornographic content moderation.
        # *   **terrorism**: terrorist content moderation.
        # *   **ad**: ad moderation.
        # *   **live**: undesirable scene moderation.
        # *   **logo**: logo moderation.
        self.scene = scene
        # The recommended subsequent operation. Valid values:
        # 
        # *   **pass**: The content passes the moderation.
        # *   **review**: The content needs to be manually reviewed.
        # *   **block**: The content needs to be blocked.
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultCensorResults(DaraModel):
    def __init__(
        self,
        censor_result: List[main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultCensorResultsCensorResult] = None,
    ):
        self.censor_result = censor_result

    def validate(self):
        if self.censor_result:
            for v1 in self.censor_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CensorResult'] = []
        if self.censor_result is not None:
            for k1 in self.censor_result:
                result['CensorResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.censor_result = []
        if m.get('CensorResult') is not None:
            for k1 in m.get('CensorResult'):
                temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultCensorResultsCensorResult()
                self.censor_result.append(temp_model.from_map(k1))

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobVensorCensorResultCensorResultsCensorResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        rate: str = None,
        scene: str = None,
        suggestion: str = None,
    ):
        # The label of the moderation result. Separate multiple labels with commas (,).
        # 
        # *   Valid values in the pornographic content moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **sexy**: sexy content.
        #     *   **porn**: pornographic content.
        # 
        # *   Valid values in the terrorist content moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **bloody**: bloody content.
        #     *   **explosion**: explosion and smoke.
        #     *   **outfit**: special costume.
        #     *   **logo**: special logo.
        #     *   **weapon**: weapon.
        #     *   **politics**: political content.
        #     *   **violence**: violence.
        #     *   **crowd**: crowd.
        #     *   **parade**: parade.
        #     *   **carcrash**: car accident.
        #     *   **flag**: flag.
        #     *   **location**: landmark.
        #     *   **others**: other content.
        # 
        # *   Valid values in the ad moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **ad**: other ads.
        #     *   **politics**: political content in text.
        #     *   **porn**: pornographic content in text.
        #     *   **abuse**: abuse in text.
        #     *   **terrorism**: terrorist content in text.
        #     *   **contraband**: prohibited content in text.
        #     *   **spam**: spam in text.
        #     *   **npx**: illegal ad.
        #     *   **qrcode**: QR code.
        #     *   **programCode**: mini program code.
        # 
        # *   Valid values in the undesirable scene moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **meaningless**: meaningless content, such as a black or white screen.
        #     *   **PIP**: picture-in-picture.
        #     *   **smoking**: smoking.
        #     *   **drivelive**: live streaming in a running vehicle.
        # 
        # *   Valid values in the logo moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **TV**: controlled logo.
        #     *   **trademark**: trademark.
        self.label = label
        # The score. Valid values: 0 to 100.
        self.rate = rate
        # The moderation scenario. Valid values:
        # 
        # *   **porn**: pornographic content moderation.
        # *   **terrorism**: terrorist content moderation.
        # *   **ad**: ad moderation.
        # *   **live**: undesirable scene moderation.
        # *   **logo**: logo moderation.
        self.scene = scene
        # The recommended subsequent operation. Valid values:
        # 
        # *   **pass**: The content passes the moderation.
        # *   **review**: The content needs to be manually reviewed.
        # *   **block**: The content needs to be blocked.
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobTitleCensorResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        rate: str = None,
        scene: str = None,
        suggestion: str = None,
    ):
        # The label of the moderation result. Separate multiple labels with commas (,). Valid values:
        # 
        # *   **normal**: normal content.
        # *   **spam**: spam.
        # *   **ad**: ads.
        # *   **abuse**: abuse content.
        # *   **flood**: excessive junk content.
        # *   **contraband**: prohibited content.
        # *   **meaningless**: meaningless content.
        self.label = label
        # The score. Valid values: 0 to 100.
        self.rate = rate
        # The moderation scenario. The value is **antispam**.
        self.scene = scene
        # The recommended subsequent operation. Valid values:
        # 
        # *   **pass**: The content passes the moderation.
        # *   **review**: The content needs to be manually reviewed.
        # *   **block**: The content needs to be blocked.
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobInput(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
    ):
        # The name of the OSS bucket in which the input file is stored.
        self.bucket = bucket
        # The OSS region in which the input file resides.
        self.location = location
        # The name of the OSS object that is used as the input file.
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobDescCensorResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        rate: str = None,
        scene: str = None,
        suggestion: str = None,
    ):
        # The label of the moderation result. Separate multiple labels with commas (,). Valid values:
        # 
        # *   **normal**: normal content.
        # *   **spam**: spam.
        # *   **ad**: ads.
        # *   **abuse**: abuse content.
        # *   **flood**: excessive junk content.
        # *   **contraband**: prohibited content.
        # *   **meaningless**: meaningless content.
        self.label = label
        # The score. Valid values: 0 to 100.
        self.rate = rate
        # The moderation scenario. The value is **antispam**.
        self.scene = scene
        # The recommended subsequent operation. Valid values:
        # 
        # *   **pass**: The content passes the moderation.
        # *   **review**: The content needs to be manually reviewed.
        # *   **block**: The content needs to be blocked.
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResults(DaraModel):
    def __init__(
        self,
        cover_image_censor_result: List[main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResultsCoverImageCensorResult] = None,
    ):
        self.cover_image_censor_result = cover_image_censor_result

    def validate(self):
        if self.cover_image_censor_result:
            for v1 in self.cover_image_censor_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CoverImageCensorResult'] = []
        if self.cover_image_censor_result is not None:
            for k1 in self.cover_image_censor_result:
                result['CoverImageCensorResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cover_image_censor_result = []
        if m.get('CoverImageCensorResult') is not None:
            for k1 in m.get('CoverImageCensorResult'):
                temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResultsCoverImageCensorResult()
                self.cover_image_censor_result.append(temp_model.from_map(k1))

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResultsCoverImageCensorResult(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
        results: main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResultsCoverImageCensorResultResults = None,
    ):
        # The OSS bucket in which the thumbnail is stored.
        self.bucket = bucket
        # The OSS region in which the thumbnail resides.
        self.location = location
        # The Object Storage Service (OSS) object that is used as the thumbnail.
        self.object = object
        # The moderation results.
        self.results = results

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        if self.results is not None:
            result['Results'] = self.results.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('Results') is not None:
            temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResultsCoverImageCensorResultResults()
            self.results = temp_model.from_map(m.get('Results'))

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResultsCoverImageCensorResultResults(DaraModel):
    def __init__(
        self,
        result: List[main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResultsCoverImageCensorResultResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResultsCoverImageCensorResultResultsResult()
                self.result.append(temp_model.from_map(k1))

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobCoverImageCensorResultsCoverImageCensorResultResultsResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        rate: str = None,
        scene: str = None,
        suggestion: str = None,
    ):
        # The label of the moderation result. Separate multiple labels with commas (,).
        # 
        # *   Valid values in the pornographic content moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **sexy**: sexy content.
        #     *   **porn**: pornographic content.
        # 
        # *   Valid values in the terrorist content moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **bloody**: bloody content.
        #     *   **explosion**: explosion and smoke.
        #     *   **outfit**: special costume.
        #     *   **logo**: special logo.
        #     *   **weapon**: weapon.
        #     *   **politics**: political content.
        #     *   **violence**: violence.
        #     *   **crowd**: crowd.
        #     *   **parade**: parade.
        #     *   **carcrash**: car accident.
        #     *   **flag**: flag.
        #     *   **location**: landmark.
        #     *   **others**: other content.
        # 
        # *   Valid values in the ad moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **ad**: other ads.
        #     *   **politics**: political content in text.
        #     *   **porn**: pornographic content in text.
        #     *   **abuse**: abuse in text.
        #     *   **terrorism**: terrorist content in text.
        #     *   **contraband**: prohibited content in text.
        #     *   **spam**: spam in text.
        #     *   **npx**: illegal ad.
        #     *   **qrcode**: QR code.
        #     *   **programCode**: mini program code.
        # 
        # *   Valid values in the undesirable scene moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **meaningless**: meaningless content, such as a black or white screen.
        #     *   **PIP**: picture-in-picture.
        #     *   **smoking**: smoking.
        #     *   **drivelive**: live streaming in a running vehicle.
        # 
        # *   Valid values in the logo moderation scenario:
        # 
        #     *   **normal**: normal content.
        #     *   **TV**: controlled logo.
        #     *   **trademark**: trademark.
        self.label = label
        # The score. Valid values: 0 to 100.
        self.rate = rate
        # The moderation scenario. Valid values:
        # 
        # *   **porn**: pornographic content moderation.
        # *   **terrorism**: terrorist content moderation.
        # *   **ad**: ad moderation.
        # *   **live**: undesirable scene moderation.
        # *   **logo**: logo moderation.
        self.scene = scene
        # The overall result of the moderation job. Valid values:
        # 
        # *   **pass**: The content passes the moderation.
        # *   **review**: The content needs to be manually reviewed.
        # *   **block**: The content needs to be blocked.
        # 
        # >  If the moderation result of any type of content is review, the overall result is review. If the moderation result of any type of content is block, the overall result is block.
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class QueryMediaCensorJobListResponseBodyMediaCensorJobListMediaCensorJobBarrageCensorResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        rate: str = None,
        scene: str = None,
        suggestion: str = None,
    ):
        # The label of the moderation result. Separate multiple labels with commas (,). Valid values:
        # 
        # *   **normal**: normal content.
        # *   **spam**: spam.
        # *   **ad**: ads.
        # *   **abuse**: abuse content.
        # *   **flood**: excessive junk content.
        # *   **contraband**: prohibited content.
        # *   **meaningless**: meaningless content.
        self.label = label
        # The score. Valid values: 0 to 100.
        self.rate = rate
        # The moderation scenario. The value is **antispam**.
        self.scene = scene
        # The recommended subsequent operation. Valid values:
        # 
        # *   **pass**: The content passes the moderation.
        # *   **review**: The content needs to be manually reviewed.
        # *   **block**: The content needs to be blocked.
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

