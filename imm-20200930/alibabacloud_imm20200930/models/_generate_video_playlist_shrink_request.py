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
        # **Leave this parameter empty unless you have specific requirements.**
        # 
        # The China authorization configuration. This parameter is optional. For more information, see [Use Chinese authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The OSS URI of the Master Playlist.
        # 
        # The OSS URI follows the format oss://${Bucket}/${Object}, where ${Bucket} is the name of the OSS bucket in the same region as the current project, and ${Object} is the full path of the file with the ".m3u8" extension.
        # > If the playlist has subtitle input or multiple Target outputs, MasterURI is required. The subtitle URI or Target URI must be in the same directory as or a subdirectory of MasterURI.
        self.master_uri = master_uri
        # The message notification configuration. Click Notification for details. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The overwrite policy when a Media Playlist already exists. Valid values:
        # 
        # - overwrite (default): overwrites the existing Media Playlist.
        # - skip-existing: skips generation and retains the existing Media Playlist.
        self.overwrite_policy = overwrite_policy
        # The project name. For information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The duration for generating the playlist. Unit: seconds. Valid values:
        # 
        # - 0 (default) or empty: continues until the end of the source video.
        # 
        # - A value greater than 0: continues for the specified duration from the start time of the playlist.
        # 
        # > If the time point corresponding to the specified parameter exceeds the end of the source video, the default value is used.
        self.source_duration = source_duration
        # The start time for generating the playlist. Unit: seconds. Valid values:
        # 
        # - 0 (default) or empty: starts from the beginning of the source video.
        # 
        # - A value greater than 0: starts from the specified time point in the source video.
        # 
        # > You can set this parameter together with **SourceDuration** to generate a playlist for a specific portion of the source video.
        self.source_start_time = source_start_time
        # The list of subtitles to add. This parameter is empty by default. A maximum of two subtitles are supported.
        self.source_subtitles_shrink = source_subtitles_shrink
        # The OSS URI of the video.
        # 
        # The OSS URI follows the format oss://${Bucket}/${Object}, where ${Bucket} is the name of the OSS bucket in the same region as the current project, and ${Object} is the full path of the file including the file name extension.
        # > Only OSS buckets with Standard storage class are supported.
        # > Buckets with hotlink protection whitelist configured are not supported.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The OSS object [tags](https://help.aliyun.com/document_detail/106678.html) to add to the generated TS files. You can use tags to control the lifecycle of OSS files.
        self.tags_shrink = tags_shrink
        # The array of just-in-time transcoding playlists. The maximum array length is 6. Each Target corresponds to at most one video Media Playlist and one or more subtitle Media Playlists.
        # > If more than one Target is configured, the **MasterURI** parameter must not be empty.
        # 
        # This parameter is required.
        self.targets_shrink = targets_shrink
        # The custom information, which is returned in asynchronous message notifications. This allows you to associate message notifications with specific processes in your system. Maximum length: 2,048 bytes.
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

