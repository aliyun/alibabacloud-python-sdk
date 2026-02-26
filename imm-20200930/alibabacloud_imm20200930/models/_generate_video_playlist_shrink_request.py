# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateVideoPlaylistShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        master_uri: str = None,
        notification_shrink: str = None,
        overwrite_policy: str = None,
        project_name: str = None,
        source_duration: float = None,
        source_start_time: float = None,
        source_subtitles_shrink: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        targets_shrink: str = None,
        user_data: str = None,
    ):
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The OSS path of the master playlist.
        # 
        # The OSS path must be in the oss://${Bucket}/${Object} format. ${Bucket} specifies the name of the OSS bucket that is in the same region as the current project. ${Object} specifies the full path of the file that is suffixed with .m3u8.
        # 
        # >  If a playlist contains subtitles or multiple outputs, the MasterURI parameter is required and the URI of subtitle files or outputs must be in the directory specified by the MasterURI parameter or its subdirectory.
        self.master_uri = master_uri
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The overwrite policy when the media playlist exists. Valid values:
        # 
        # *   overwrite (default): overwrites an existing media playlist.
        # *   skip-existing: skips generation and retains the existing media playlist.
        self.overwrite_policy = overwrite_policy
        # The project name.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The period of time during which the playlist is generated. Unit: seconds.
        # 
        # *   If you set this parameter to 0 (default) or leave this parameter empty, a playlist is generated until the end time of the source video.
        # *   If you set this parameter to a value greater than 0, a playlist is generated for the specified period of time from the start time that you specify.
        # 
        # >  If you set this parameter to a value that exceeds the end time of a source video, use the default value.
        self.source_duration = source_duration
        # The time when the playlist starts to generate. Unit: seconds.
        # 
        # *   If you set this parameter to 0 (default) or leave this parameter empty, the start time of the source video is used as the time when a playlist starts to generate.
        # *   If you set this parameter to a value greater than 0, the time when a playlist starts to generate is the specified point in time.
        # 
        # >  If you use this parameter together with the **SourceDuration** parameter, a playlist can be generated based on the partial content of a source video.
        self.source_start_time = source_start_time
        # The subtitle files. By default, this parameter is left empty. Up to two subtitle files are supported.
        self.source_subtitles_shrink = source_subtitles_shrink
        # The OSS path of the video file.
        # 
        # The OSS path must be in the oss://${Bucket}/${Object} format. ${Bucket} specifies the name of the OSS bucket that is in the same region as the current project. ${Object} specifies the full path of the file that contains the file name extension.
        # 
        # >  Only OSS buckets of the Standard storage class are supported. OSS buckets for which hotlink protection whitelists are configured are not supported.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The [tags](https://help.aliyun.com/document_detail/106678.html) that you want to add to a TS file in OSS. You can use tags to manage the lifecycles of TS files in OSS.
        self.tags_shrink = tags_shrink
        # The array of live transcoding playlists. The maximum length of the array is 6. Each element corresponds to at most one video media playlist and one or more subtitle media playlists.
        # 
        # >  If the array contains more than one element, the **MasterURI** parameter cannot be left empty.
        # 
        # This parameter is required.
        self.targets_shrink = targets_shrink
        # The custom user information, which is returned in asynchronous notifications to help you handle the notifications in the system. The maximum length of a notification is 2048 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.master_uri is not None:
            result['MasterURI'] = self.master_uri

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.overwrite_policy is not None:
            result['OverwritePolicy'] = self.overwrite_policy

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_duration is not None:
            result['SourceDuration'] = self.source_duration

        if self.source_start_time is not None:
            result['SourceStartTime'] = self.source_start_time

        if self.source_subtitles_shrink is not None:
            result['SourceSubtitles'] = self.source_subtitles_shrink

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('MasterURI') is not None:
            self.master_uri = m.get('MasterURI')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('OverwritePolicy') is not None:
            self.overwrite_policy = m.get('OverwritePolicy')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceDuration') is not None:
            self.source_duration = m.get('SourceDuration')

        if m.get('SourceStartTime') is not None:
            self.source_start_time = m.get('SourceStartTime')

        if m.get('SourceSubtitles') is not None:
            self.source_subtitles_shrink = m.get('SourceSubtitles')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

