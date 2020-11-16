# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_live20161101 import models as live_20161101_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "cn-qingdao": "live.aliyuncs.com",
            "cn-beijing": "live.aliyuncs.com",
            "cn-hangzhou": "live.aliyuncs.com",
            "cn-shanghai": "live.aliyuncs.com",
            "cn-shenzhen": "live.aliyuncs.com",
            "ap-southeast-1": "live.aliyuncs.com",
            "ap-southeast-5": "live.aliyuncs.com",
            "ap-northeast-1": "live.aliyuncs.com",
            "eu-central-1": "live.aliyuncs.com",
            "ap-south-1": "live.aliyuncs.com",
            "ap-northeast-2-pop": "live.ap-southeast-1.aliyuncs.com",
            "ap-southeast-2": "live.ap-southeast-1.aliyuncs.com",
            "ap-southeast-3": "live.ap-southeast-1.aliyuncs.com",
            "cn-beijing-finance-1": "live.aliyuncs.com",
            "cn-beijing-finance-pop": "live.aliyuncs.com",
            "cn-beijing-gov-1": "live.aliyuncs.com",
            "cn-beijing-nu16-b01": "live.aliyuncs.com",
            "cn-chengdu": "live.aliyuncs.com",
            "cn-edge-1": "live.aliyuncs.com",
            "cn-fujian": "live.aliyuncs.com",
            "cn-haidian-cm12-c01": "live.aliyuncs.com",
            "cn-hangzhou-bj-b01": "live.aliyuncs.com",
            "cn-hangzhou-finance": "live.aliyuncs.com",
            "cn-hangzhou-internal-prod-1": "live.aliyuncs.com",
            "cn-hangzhou-internal-test-1": "live.aliyuncs.com",
            "cn-hangzhou-internal-test-2": "live.aliyuncs.com",
            "cn-hangzhou-internal-test-3": "live.aliyuncs.com",
            "cn-hangzhou-test-306": "live.aliyuncs.com",
            "cn-hongkong": "live.aliyuncs.com",
            "cn-hongkong-finance-pop": "live.aliyuncs.com",
            "cn-huhehaote": "live.aliyuncs.com",
            "cn-north-2-gov-1": "live.aliyuncs.com",
            "cn-qingdao-nebula": "live.aliyuncs.com",
            "cn-shanghai-et15-b01": "live.aliyuncs.com",
            "cn-shanghai-et2-b01": "live.aliyuncs.com",
            "cn-shanghai-finance-1": "live.aliyuncs.com",
            "cn-shanghai-inner": "live.aliyuncs.com",
            "cn-shanghai-internal-test-1": "live.aliyuncs.com",
            "cn-shenzhen-finance-1": "live.aliyuncs.com",
            "cn-shenzhen-inner": "live.aliyuncs.com",
            "cn-shenzhen-st4-d01": "live.aliyuncs.com",
            "cn-shenzhen-su18-b01": "live.aliyuncs.com",
            "cn-wuhan": "live.aliyuncs.com",
            "cn-yushanfang": "live.aliyuncs.com",
            "cn-zhangbei-na61-b01": "live.aliyuncs.com",
            "cn-zhangjiakou": "live.aliyuncs.com",
            "cn-zhangjiakou-na62-a01": "live.aliyuncs.com",
            "cn-zhengzhou-nebula-1": "live.aliyuncs.com",
            "eu-west-1": "live.ap-southeast-1.aliyuncs.com",
            "eu-west-1-oxs": "live.ap-southeast-1.aliyuncs.com",
            "me-east-1": "live.ap-southeast-1.aliyuncs.com",
            "rus-west-1-pop": "live.ap-southeast-1.aliyuncs.com",
            "us-east-1": "live.ap-southeast-1.aliyuncs.com",
            "us-west-1": "live.ap-southeast-1.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("live", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def add_live_asrconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveASRConfigResponse().from_map(self.do_request("AddLiveASRConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_asrconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_asrconfig_with_options(request, runtime)

    def describe_live_asr_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveAsrConfigResponse().from_map(self.do_request("DescribeLiveAsrConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_asr_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_asr_config_with_options(request, runtime)

    def delete_live_asrconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveASRConfigResponse().from_map(self.do_request("DeleteLiveASRConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_asrconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_asrconfig_with_options(request, runtime)

    def update_live_asrconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateLiveASRConfigResponse().from_map(self.do_request("UpdateLiveASRConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_live_asrconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_asrconfig_with_options(request, runtime)

    def delete_mix_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteMixStreamResponse().from_map(self.do_request("DeleteMixStream", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_mix_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mix_stream_with_options(request, runtime)

    def update_mix_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateMixStreamResponse().from_map(self.do_request("UpdateMixStream", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_mix_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_mix_stream_with_options(request, runtime)

    def create_mix_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.CreateMixStreamResponse().from_map(self.do_request("CreateMixStream", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def create_mix_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mix_stream_with_options(request, runtime)

    def describe_mix_stream_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeMixStreamListResponse().from_map(self.do_request("DescribeMixStreamList", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_mix_stream_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mix_stream_list_with_options(request, runtime)

    def add_rts_live_stream_transcode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddRtsLiveStreamTranscodeResponse().from_map(self.do_request("AddRtsLiveStreamTranscode", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_rts_live_stream_transcode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_rts_live_stream_transcode_with_options(request, runtime)

    def describe_live_domain_time_shift_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainTimeShiftDataResponse().from_map(self.do_request("DescribeLiveDomainTimeShiftData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_time_shift_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_time_shift_data_with_options(request, runtime)

    def delete_html_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteHtmlResourceResponse().from_map(self.do_request("DeleteHtmlResource", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_html_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_html_resource_with_options(request, runtime)

    def describe_html_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeHtmlResourceResponse().from_map(self.do_request("DescribeHtmlResource", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_html_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_html_resource_with_options(request, runtime)

    def control_html_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ControlHtmlResourceResponse().from_map(self.do_request("ControlHtmlResource", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def control_html_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.control_html_resource_with_options(request, runtime)

    def edit_html_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.EditHtmlResourceResponse().from_map(self.do_request("EditHtmlResource", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def edit_html_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_html_resource_with_options(request, runtime)

    def describe_live_user_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveUserTagsResponse().from_map(self.do_request("DescribeLiveUserTags", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_user_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_user_tags_with_options(request, runtime)

    def un_tag_live_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UnTagLiveResourcesResponse().from_map(self.do_request("UnTagLiveResources", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def un_tag_live_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_tag_live_resources_with_options(request, runtime)

    def tag_live_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.TagLiveResourcesResponse().from_map(self.do_request("TagLiveResources", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def tag_live_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_live_resources_with_options(request, runtime)

    def describe_live_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveTagResourcesResponse().from_map(self.do_request("DescribeLiveTagResources", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_tag_resources_with_options(request, runtime)

    def add_live_audio_audit_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveAudioAuditConfigResponse().from_map(self.do_request("AddLiveAudioAuditConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_audio_audit_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_audio_audit_config_with_options(request, runtime)

    def delete_live_audio_audit_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveAudioAuditConfigResponse().from_map(self.do_request("DeleteLiveAudioAuditConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_audio_audit_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_audio_audit_config_with_options(request, runtime)

    def describe_live_audio_audit_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveAudioAuditConfigResponse().from_map(self.do_request("DescribeLiveAudioAuditConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_audio_audit_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_audio_audit_config_with_options(request, runtime)

    def update_live_audio_audit_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateLiveAudioAuditConfigResponse().from_map(self.do_request("UpdateLiveAudioAuditConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_live_audio_audit_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_audio_audit_config_with_options(request, runtime)

    def add_live_audio_audit_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveAudioAuditNotifyConfigResponse().from_map(self.do_request("AddLiveAudioAuditNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_audio_audit_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_audio_audit_notify_config_with_options(request, runtime)

    def delete_live_audio_audit_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse().from_map(self.do_request("DeleteLiveAudioAuditNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_audio_audit_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_audio_audit_notify_config_with_options(request, runtime)

    def describe_live_audio_audit_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse().from_map(self.do_request("DescribeLiveAudioAuditNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_audio_audit_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_audio_audit_notify_config_with_options(request, runtime)

    def update_live_audio_audit_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse().from_map(self.do_request("UpdateLiveAudioAuditNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_live_audio_audit_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_audio_audit_notify_config_with_options(request, runtime)

    def describe_live_domain_push_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainPushTrafficDataResponse().from_map(self.do_request("DescribeLiveDomainPushTrafficData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_push_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_push_traffic_data_with_options(request, runtime)

    def describe_live_domain_push_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainPushBpsDataResponse().from_map(self.do_request("DescribeLiveDomainPushBpsData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_push_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_push_bps_data_with_options(request, runtime)

    def set_caster_sync_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SetCasterSyncGroupResponse().from_map(self.do_request("SetCasterSyncGroup", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def set_caster_sync_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_caster_sync_group_with_options(request, runtime)

    def describe_caster_sync_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterSyncGroupResponse().from_map(self.do_request("DescribeCasterSyncGroup", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_sync_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_sync_group_with_options(request, runtime)

    def describe_live_detect_porn_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDetectPornDataResponse().from_map(self.do_request("DescribeLiveDetectPornData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_detect_porn_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_detect_porn_data_with_options(request, runtime)

    def delete_live_real_time_log_logstore_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse().from_map(self.do_request("DeleteLiveRealTimeLogLogstore", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def delete_live_real_time_log_logstore(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_real_time_log_logstore_with_options(request, runtime)

    def disable_live_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DisableLiveRealtimeLogDeliveryResponse().from_map(self.do_request("DisableLiveRealtimeLogDelivery", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def disable_live_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_live_realtime_log_delivery_with_options(request, runtime)

    def enable_live_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.EnableLiveRealtimeLogDeliveryResponse().from_map(self.do_request("EnableLiveRealtimeLogDelivery", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def enable_live_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_live_realtime_log_delivery_with_options(request, runtime)

    def list_live_realtime_log_delivery_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse().from_map(self.do_request("ListLiveRealtimeLogDeliveryDomains", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def list_live_realtime_log_delivery_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_realtime_log_delivery_domains_with_options(request, runtime)

    def modify_live_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse().from_map(self.do_request("ModifyLiveRealtimeLogDelivery", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def modify_live_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_live_realtime_log_delivery_with_options(request, runtime)

    def describe_live_realtime_delivery_acc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse().from_map(self.do_request("DescribeLiveRealtimeDeliveryAcc", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_realtime_delivery_acc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_realtime_delivery_acc_with_options(request, runtime)

    def describe_live_realtime_log_authorized_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse().from_map(self.do_request("DescribeLiveRealtimeLogAuthorized", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def describe_live_realtime_log_authorized(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_realtime_log_authorized_with_options(request, runtime)

    def list_live_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ListLiveRealtimeLogDeliveryResponse().from_map(self.do_request("ListLiveRealtimeLogDelivery", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def list_live_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_realtime_log_delivery_with_options(request, runtime)

    def list_live_realtime_log_delivery_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse().from_map(self.do_request("ListLiveRealtimeLogDeliveryInfos", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def list_live_realtime_log_delivery_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_realtime_log_delivery_infos_with_options(request, runtime)

    def describe_live_domain_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse().from_map(self.do_request("DescribeLiveDomainRealtimeLogDelivery", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def describe_live_domain_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_realtime_log_delivery_with_options(request, runtime)

    def delete_live_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse().from_map(self.do_request("DeleteLiveRealtimeLogDelivery", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def delete_live_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_realtime_log_delivery_with_options(request, runtime)

    def create_live_real_time_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.CreateLiveRealTimeLogDeliveryResponse().from_map(self.do_request("CreateLiveRealTimeLogDelivery", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def create_live_real_time_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_real_time_log_delivery_with_options(request, runtime)

    def describe_live_domain_limit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainLimitResponse().from_map(self.do_request("DescribeLiveDomainLimit", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_limit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_limit_with_options(request, runtime)

    def describe_live_domain_bps_data_by_time_stamp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse().from_map(self.do_request("DescribeLiveDomainBpsDataByTimeStamp", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_bps_data_by_time_stamp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_bps_data_by_time_stamp_with_options(request, runtime)

    def describe_live_stream_transcode_stream_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse().from_map(self.do_request("DescribeLiveStreamTranscodeStreamNum", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_transcode_stream_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_transcode_stream_num_with_options(request, runtime)

    def update_live_top_level_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateLiveTopLevelDomainResponse().from_map(self.do_request("UpdateLiveTopLevelDomain", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_live_top_level_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_top_level_domain_with_options(request, runtime)

    def describe_live_domain_certificate_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainCertificateInfoResponse().from_map(self.do_request("DescribeLiveDomainCertificateInfo", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_certificate_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_certificate_info_with_options(request, runtime)

    def modify_live_domain_schdm_by_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse().from_map(self.do_request("ModifyLiveDomainSchdmByProperty", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def modify_live_domain_schdm_by_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_live_domain_schdm_by_property_with_options(request, runtime)

    def set_live_stream_optimized_feature_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse().from_map(self.do_request("SetLiveStreamOptimizedFeatureConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def set_live_stream_optimized_feature_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_stream_optimized_feature_config_with_options(request, runtime)

    def describe_live_stream_optimized_feature_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse().from_map(self.do_request("DescribeLiveStreamOptimizedFeatureConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_optimized_feature_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_optimized_feature_config_with_options(request, runtime)

    def set_live_stream_delay_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SetLiveStreamDelayConfigResponse().from_map(self.do_request("SetLiveStreamDelayConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def set_live_stream_delay_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_stream_delay_config_with_options(request, runtime)

    def describe_live_stream_delay_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamDelayConfigResponse().from_map(self.do_request("DescribeLiveStreamDelayConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_delay_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_delay_config_with_options(request, runtime)

    def describe_live_domain_online_user_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainOnlineUserNumResponse().from_map(self.do_request("DescribeLiveDomainOnlineUserNum", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_online_user_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_online_user_num_with_options(request, runtime)

    def describe_live_domain_frame_rate_and_bit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse().from_map(self.do_request("DescribeLiveDomainFrameRateAndBitRateData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_frame_rate_and_bit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_frame_rate_and_bit_rate_data_with_options(request, runtime)

    def set_board_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SetBoardCallbackResponse().from_map(self.do_request("SetBoardCallback", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def set_board_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_board_callback_with_options(request, runtime)

    def describe_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeRecordsResponse().from_map(self.do_request("DescribeRecords", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_records_with_options(request, runtime)

    def describe_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeRecordResponse().from_map(self.do_request("DescribeRecord", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_record_with_options(request, runtime)

    def complete_board_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.CompleteBoardRecordResponse().from_map(self.do_request("CompleteBoardRecord", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def complete_board_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complete_board_record_with_options(request, runtime)

    def start_board_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.StartBoardRecordResponse().from_map(self.do_request("StartBoardRecord", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def start_board_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_board_record_with_options(request, runtime)

    def apply_record_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ApplyRecordTokenResponse().from_map(self.do_request("ApplyRecordToken", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def apply_record_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_record_token_with_options(request, runtime)

    def update_board_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateBoardCallbackResponse().from_map(self.do_request("UpdateBoardCallback", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_board_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_board_callback_with_options(request, runtime)

    def describe_live_domain_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainMappingResponse().from_map(self.do_request("DescribeLiveDomainMapping", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def describe_live_domain_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_mapping_with_options(request, runtime)

    def stop_live_index_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.StopLiveIndexResponse().from_map(self.do_request("StopLiveIndex", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def stop_live_index(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_live_index_with_options(request, runtime)

    def start_live_index_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.StartLiveIndexResponse().from_map(self.do_request("StartLiveIndex", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def start_live_index(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_live_index_with_options(request, runtime)

    def real_time_snapshot_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.RealTimeSnapshotCommandResponse().from_map(self.do_request("RealTimeSnapshotCommand", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def real_time_snapshot_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.real_time_snapshot_command_with_options(request, runtime)

    def describe_live_top_domains_by_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveTopDomainsByFlowResponse().from_map(self.do_request("DescribeLiveTopDomainsByFlow", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_top_domains_by_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_top_domains_by_flow_with_options(request, runtime)

    def describe_live_domain_real_time_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse().from_map(self.do_request("DescribeLiveDomainRealTimeBpsData", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def describe_live_domain_real_time_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_real_time_bps_data_with_options(request, runtime)

    def describe_live_domain_real_time_http_code_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse().from_map(self.do_request("DescribeLiveDomainRealTimeHttpCodeData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_real_time_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_real_time_http_code_data_with_options(request, runtime)

    def describe_live_domain_real_time_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse().from_map(self.do_request("DescribeLiveDomainRealTimeTrafficData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_real_time_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_real_time_traffic_data_with_options(request, runtime)

    def add_live_domain_play_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveDomainPlayMappingResponse().from_map(self.do_request("AddLiveDomainPlayMapping", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_domain_play_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_domain_play_mapping_with_options(request, runtime)

    def delete_live_lazy_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse().from_map(self.do_request("DeleteLiveLazyPullStreamInfoConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_lazy_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_lazy_pull_stream_info_config_with_options(request, runtime)

    def describe_live_lazy_pull_stream_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveLazyPullStreamConfigResponse().from_map(self.do_request("DescribeLiveLazyPullStreamConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_lazy_pull_stream_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_lazy_pull_stream_config_with_options(request, runtime)

    def set_live_lazy_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse().from_map(self.do_request("SetLiveLazyPullStreamInfoConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def set_live_lazy_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_lazy_pull_stream_info_config_with_options(request, runtime)

    def update_caster_scene_audio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateCasterSceneAudioResponse().from_map(self.do_request("UpdateCasterSceneAudio", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_caster_scene_audio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_caster_scene_audio_with_options(request, runtime)

    def set_caster_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SetCasterChannelResponse().from_map(self.do_request("SetCasterChannel", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def set_caster_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_caster_channel_with_options(request, runtime)

    def describe_caster_scene_audio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterSceneAudioResponse().from_map(self.do_request("DescribeCasterSceneAudio", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_scene_audio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_scene_audio_with_options(request, runtime)

    def describe_caster_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterChannelsResponse().from_map(self.do_request("DescribeCasterChannels", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_channels_with_options(request, runtime)

    def update_board_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateBoardResponse().from_map(self.do_request("UpdateBoard", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_board(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_board_with_options(request, runtime)

    def join_board_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.JoinBoardResponse().from_map(self.do_request("JoinBoard", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def join_board(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_board_with_options(request, runtime)

    def describe_board_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeBoardSnapshotResponse().from_map(self.do_request("DescribeBoardSnapshot", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_board_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_board_snapshot_with_options(request, runtime)

    def describe_boards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeBoardsResponse().from_map(self.do_request("DescribeBoards", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_boards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_boards_with_options(request, runtime)

    def describe_board_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeBoardEventsResponse().from_map(self.do_request("DescribeBoardEvents", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_board_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_board_events_with_options(request, runtime)

    def delete_board_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteBoardResponse().from_map(self.do_request("DeleteBoard", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_board(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_board_with_options(request, runtime)

    def create_board_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.CreateBoardResponse().from_map(self.do_request("CreateBoard", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def create_board(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_board_with_options(request, runtime)

    def complete_board_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.CompleteBoardResponse().from_map(self.do_request("CompleteBoard", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def complete_board(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complete_board_with_options(request, runtime)

    def apply_board_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ApplyBoardTokenResponse().from_map(self.do_request("ApplyBoardToken", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def apply_board_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_board_token_with_options(request, runtime)

    def describe_live_stream_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamCountResponse().from_map(self.do_request("DescribeLiveStreamCount", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def describe_live_stream_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_count_with_options(request, runtime)

    def describe_live_certificate_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveCertificateDetailResponse().from_map(self.do_request("DescribeLiveCertificateDetail", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_certificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_certificate_detail_with_options(request, runtime)

    def describe_hls_live_stream_real_time_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse().from_map(self.do_request("DescribeHlsLiveStreamRealTimeBpsData", "HTTPS", "GET", "2016-11-01", "AK", request.to_map(), None, runtime))

    def describe_hls_live_stream_real_time_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hls_live_stream_real_time_bps_data_with_options(request, runtime)

    def stop_live_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.StopLiveDomainResponse().from_map(self.do_request("StopLiveDomain", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def stop_live_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_live_domain_with_options(request, runtime)

    def start_live_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.StartLiveDomainResponse().from_map(self.do_request("StartLiveDomain", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def start_live_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_live_domain_with_options(request, runtime)

    def set_live_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SetLiveDomainCertificateResponse().from_map(self.do_request("SetLiveDomainCertificate", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def set_live_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_domain_certificate_with_options(request, runtime)

    def batch_set_live_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.BatchSetLiveDomainConfigsResponse().from_map(self.do_request("BatchSetLiveDomainConfigs", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def batch_set_live_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_live_domain_configs_with_options(request, runtime)

    def describe_live_certificate_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveCertificateListResponse().from_map(self.do_request("DescribeLiveCertificateList", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_certificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_certificate_list_with_options(request, runtime)

    def delete_live_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveDomainResponse().from_map(self.do_request("DeleteLiveDomain", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_domain_with_options(request, runtime)

    def describe_live_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainConfigsResponse().from_map(self.do_request("DescribeLiveDomainConfigs", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_configs_with_options(request, runtime)

    def add_live_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveDomainResponse().from_map(self.do_request("AddLiveDomain", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_domain_with_options(request, runtime)

    def describe_live_domain_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainDetailResponse().from_map(self.do_request("DescribeLiveDomainDetail", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_detail_with_options(request, runtime)

    def batch_delete_live_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.BatchDeleteLiveDomainConfigsResponse().from_map(self.do_request("BatchDeleteLiveDomainConfigs", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def batch_delete_live_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_live_domain_configs_with_options(request, runtime)

    def describe_room_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeRoomStatusResponse().from_map(self.do_request("DescribeRoomStatus", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_room_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_room_status_with_options(request, runtime)

    def describe_room_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeRoomListResponse().from_map(self.do_request("DescribeRoomList", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_room_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_room_list_with_options(request, runtime)

    def describe_room_kickout_user_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeRoomKickoutUserListResponse().from_map(self.do_request("DescribeRoomKickoutUserList", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_room_kickout_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_room_kickout_user_list_with_options(request, runtime)

    def send_room_user_notification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SendRoomUserNotificationResponse().from_map(self.do_request("SendRoomUserNotification", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def send_room_user_notification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_room_user_notification_with_options(request, runtime)

    def describe_forbid_push_stream_room_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeForbidPushStreamRoomListResponse().from_map(self.do_request("DescribeForbidPushStreamRoomList", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_forbid_push_stream_room_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_forbid_push_stream_room_list_with_options(request, runtime)

    def send_room_notification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SendRoomNotificationResponse().from_map(self.do_request("SendRoomNotification", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def send_room_notification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_room_notification_with_options(request, runtime)

    def forbid_push_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ForbidPushStreamResponse().from_map(self.do_request("ForbidPushStream", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def forbid_push_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.forbid_push_stream_with_options(request, runtime)

    def delete_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteRoomResponse().from_map(self.do_request("DeleteRoom", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_room_with_options(request, runtime)

    def create_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.CreateRoomResponse().from_map(self.do_request("CreateRoom", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def create_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_room_with_options(request, runtime)

    def allow_push_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AllowPushStreamResponse().from_map(self.do_request("AllowPushStream", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def allow_push_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allow_push_stream_with_options(request, runtime)

    def describe_live_user_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveUserDomainsResponse().from_map(self.do_request("DescribeLiveUserDomains", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_user_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_user_domains_with_options(request, runtime)

    def describe_caster_rtc_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterRtcInfoResponse().from_map(self.do_request("DescribeCasterRtcInfo", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_rtc_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_rtc_info_with_options(request, runtime)

    def describe_up_bps_peak_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeUpBpsPeakDataResponse().from_map(self.do_request("DescribeUpBpsPeakData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_up_bps_peak_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_up_bps_peak_data_with_options(request, runtime)

    def describe_up_bps_peak_of_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeUpBpsPeakOfLineResponse().from_map(self.do_request("DescribeUpBpsPeakOfLine", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_up_bps_peak_of_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_up_bps_peak_of_line_with_options(request, runtime)

    def describe_up_peak_publish_stream_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeUpPeakPublishStreamDataResponse().from_map(self.do_request("DescribeUpPeakPublishStreamData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_up_peak_publish_stream_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_up_peak_publish_stream_data_with_options(request, runtime)

    def delete_live_domain_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveDomainMappingResponse().from_map(self.do_request("DeleteLiveDomainMapping", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_domain_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_domain_mapping_with_options(request, runtime)

    def add_live_domain_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveDomainMappingResponse().from_map(self.do_request("AddLiveDomainMapping", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_domain_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_domain_mapping_with_options(request, runtime)

    def add_caster_episode_group_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddCasterEpisodeGroupContentResponse().from_map(self.do_request("AddCasterEpisodeGroupContent", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_caster_episode_group_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_episode_group_content_with_options(request, runtime)

    def modify_caster_program_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ModifyCasterProgramResponse().from_map(self.do_request("ModifyCasterProgram", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def modify_caster_program(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_program_with_options(request, runtime)

    def modify_caster_episode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ModifyCasterEpisodeResponse().from_map(self.do_request("ModifyCasterEpisode", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def modify_caster_episode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_episode_with_options(request, runtime)

    def describe_caster_program_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterProgramResponse().from_map(self.do_request("DescribeCasterProgram", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_program(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_program_with_options(request, runtime)

    def delete_caster_program_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteCasterProgramResponse().from_map(self.do_request("DeleteCasterProgram", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_caster_program(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_program_with_options(request, runtime)

    def delete_caster_episode_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteCasterEpisodeGroupResponse().from_map(self.do_request("DeleteCasterEpisodeGroup", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_caster_episode_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_episode_group_with_options(request, runtime)

    def delete_caster_episode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteCasterEpisodeResponse().from_map(self.do_request("DeleteCasterEpisode", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_caster_episode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_episode_with_options(request, runtime)

    def add_caster_program_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddCasterProgramResponse().from_map(self.do_request("AddCasterProgram", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_caster_program(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_program_with_options(request, runtime)

    def add_caster_episode_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddCasterEpisodeGroupResponse().from_map(self.do_request("AddCasterEpisodeGroup", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_caster_episode_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_episode_group_with_options(request, runtime)

    def add_caster_episode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddCasterEpisodeResponse().from_map(self.do_request("AddCasterEpisode", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_caster_episode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_episode_with_options(request, runtime)

    def describe_live_domain_transcode_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainTranscodeDataResponse().from_map(self.do_request("DescribeLiveDomainTranscodeData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_transcode_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_transcode_data_with_options(request, runtime)

    def describe_live_domain_snapshot_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainSnapshotDataResponse().from_map(self.do_request("DescribeLiveDomainSnapshotData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_snapshot_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_snapshot_data_with_options(request, runtime)

    def describe_live_domain_record_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainRecordDataResponse().from_map(self.do_request("DescribeLiveDomainRecordData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_record_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_record_data_with_options(request, runtime)

    def real_time_record_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.RealTimeRecordCommandResponse().from_map(self.do_request("RealTimeRecordCommand", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def real_time_record_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.real_time_record_command_with_options(request, runtime)

    def describe_live_domain_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainTrafficDataResponse().from_map(self.do_request("DescribeLiveDomainTrafficData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_traffic_data_with_options(request, runtime)

    def describe_live_domain_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDomainBpsDataResponse().from_map(self.do_request("DescribeLiveDomainBpsData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_domain_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_bps_data_with_options(request, runtime)

    def add_trancode_seiwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddTrancodeSEIResponse().from_map(self.do_request("AddTrancodeSEI", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_trancode_sei(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_trancode_seiwith_options(request, runtime)

    def delete_caster_scene_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteCasterSceneConfigResponse().from_map(self.do_request("DeleteCasterSceneConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_caster_scene_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_scene_config_with_options(request, runtime)

    def add_custom_live_stream_transcode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddCustomLiveStreamTranscodeResponse().from_map(self.do_request("AddCustomLiveStreamTranscode", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_custom_live_stream_transcode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_custom_live_stream_transcode_with_options(request, runtime)

    def describe_live_record_vod_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveRecordVodConfigsResponse().from_map(self.do_request("DescribeLiveRecordVodConfigs", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_record_vod_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_record_vod_configs_with_options(request, runtime)

    def delete_live_record_vod_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveRecordVodConfigResponse().from_map(self.do_request("DeleteLiveRecordVodConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_record_vod_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_vod_config_with_options(request, runtime)

    def add_live_record_vod_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveRecordVodConfigResponse().from_map(self.do_request("AddLiveRecordVodConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_record_vod_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_record_vod_config_with_options(request, runtime)

    def modify_caster_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ModifyCasterComponentResponse().from_map(self.do_request("ModifyCasterComponent", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def modify_caster_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_component_with_options(request, runtime)

    def describe_caster_components_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterComponentsResponse().from_map(self.do_request("DescribeCasterComponents", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_components(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_components_with_options(request, runtime)

    def delete_caster_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteCasterComponentResponse().from_map(self.do_request("DeleteCasterComponent", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_caster_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_component_with_options(request, runtime)

    def add_caster_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddCasterComponentResponse().from_map(self.do_request("AddCasterComponent", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_caster_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_component_with_options(request, runtime)

    def stop_caster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.StopCasterResponse().from_map(self.do_request("StopCaster", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def stop_caster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_caster_with_options(request, runtime)

    def start_caster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.StartCasterResponse().from_map(self.do_request("StartCaster", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def start_caster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_caster_with_options(request, runtime)

    def describe_live_stream_history_user_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamHistoryUserNumResponse().from_map(self.do_request("DescribeLiveStreamHistoryUserNum", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_history_user_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_history_user_num_with_options(request, runtime)

    def update_caster_scene_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateCasterSceneConfigResponse().from_map(self.do_request("UpdateCasterSceneConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_caster_scene_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_caster_scene_config_with_options(request, runtime)

    def stop_caster_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.StopCasterSceneResponse().from_map(self.do_request("StopCasterScene", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def stop_caster_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_caster_scene_with_options(request, runtime)

    def start_caster_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.StartCasterSceneResponse().from_map(self.do_request("StartCasterScene", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def start_caster_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_caster_scene_with_options(request, runtime)

    def set_caster_scene_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SetCasterSceneConfigResponse().from_map(self.do_request("SetCasterSceneConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def set_caster_scene_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_caster_scene_config_with_options(request, runtime)

    def set_caster_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SetCasterConfigResponse().from_map(self.do_request("SetCasterConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def set_caster_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_caster_config_with_options(request, runtime)

    def modify_caster_video_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ModifyCasterVideoResourceResponse().from_map(self.do_request("ModifyCasterVideoResource", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def modify_caster_video_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_video_resource_with_options(request, runtime)

    def modify_caster_layout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ModifyCasterLayoutResponse().from_map(self.do_request("ModifyCasterLayout", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def modify_caster_layout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_layout_with_options(request, runtime)

    def effect_caster_video_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.EffectCasterVideoResourceResponse().from_map(self.do_request("EffectCasterVideoResource", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def effect_caster_video_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.effect_caster_video_resource_with_options(request, runtime)

    def effect_caster_urgent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.EffectCasterUrgentResponse().from_map(self.do_request("EffectCasterUrgent", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def effect_caster_urgent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.effect_caster_urgent_with_options(request, runtime)

    def describe_caster_video_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterVideoResourcesResponse().from_map(self.do_request("DescribeCasterVideoResources", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_video_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_video_resources_with_options(request, runtime)

    def describe_caster_stream_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterStreamUrlResponse().from_map(self.do_request("DescribeCasterStreamUrl", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_stream_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_stream_url_with_options(request, runtime)

    def describe_caster_scenes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterScenesResponse().from_map(self.do_request("DescribeCasterScenes", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_scenes_with_options(request, runtime)

    def describe_casters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCastersResponse().from_map(self.do_request("DescribeCasters", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_casters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_casters_with_options(request, runtime)

    def describe_caster_layouts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterLayoutsResponse().from_map(self.do_request("DescribeCasterLayouts", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_layouts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_layouts_with_options(request, runtime)

    def describe_caster_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeCasterConfigResponse().from_map(self.do_request("DescribeCasterConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_caster_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_config_with_options(request, runtime)

    def delete_caster_video_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteCasterVideoResourceResponse().from_map(self.do_request("DeleteCasterVideoResource", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_caster_video_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_video_resource_with_options(request, runtime)

    def delete_caster_layout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteCasterLayoutResponse().from_map(self.do_request("DeleteCasterLayout", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_caster_layout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_layout_with_options(request, runtime)

    def delete_caster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteCasterResponse().from_map(self.do_request("DeleteCaster", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_caster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_with_options(request, runtime)

    def create_caster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.CreateCasterResponse().from_map(self.do_request("CreateCaster", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def create_caster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_caster_with_options(request, runtime)

    def copy_caster_scene_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.CopyCasterSceneConfigResponse().from_map(self.do_request("CopyCasterSceneConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def copy_caster_scene_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_caster_scene_config_with_options(request, runtime)

    def copy_caster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.CopyCasterResponse().from_map(self.do_request("CopyCaster", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def copy_caster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_caster_with_options(request, runtime)

    def add_caster_video_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddCasterVideoResourceResponse().from_map(self.do_request("AddCasterVideoResource", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_caster_video_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_video_resource_with_options(request, runtime)

    def add_caster_layout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddCasterLayoutResponse().from_map(self.do_request("AddCasterLayout", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_caster_layout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_layout_with_options(request, runtime)

    def describe_live_pull_stream_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLivePullStreamConfigResponse().from_map(self.do_request("DescribeLivePullStreamConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_pull_stream_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_pull_stream_config_with_options(request, runtime)

    def delete_live_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLivePullStreamInfoConfigResponse().from_map(self.do_request("DeleteLivePullStreamInfoConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_pull_stream_info_config_with_options(request, runtime)

    def add_live_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLivePullStreamInfoConfigResponse().from_map(self.do_request("AddLivePullStreamInfoConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_pull_stream_info_config_with_options(request, runtime)

    def describe_live_stream_bit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamBitRateDataResponse().from_map(self.do_request("DescribeLiveStreamBitRateData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_bit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_bit_rate_data_with_options(request, runtime)

    def add_live_detect_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveDetectNotifyConfigResponse().from_map(self.do_request("AddLiveDetectNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_detect_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_detect_notify_config_with_options(request, runtime)

    def add_live_snapshot_detect_porn_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveSnapshotDetectPornConfigResponse().from_map(self.do_request("AddLiveSnapshotDetectPornConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_snapshot_detect_porn_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_snapshot_detect_porn_config_with_options(request, runtime)

    def delete_live_detect_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveDetectNotifyConfigResponse().from_map(self.do_request("DeleteLiveDetectNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_detect_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_detect_notify_config_with_options(request, runtime)

    def describe_live_detect_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveDetectNotifyConfigResponse().from_map(self.do_request("DescribeLiveDetectNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_detect_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_detect_notify_config_with_options(request, runtime)

    def delete_live_snapshot_detect_porn_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse().from_map(self.do_request("DeleteLiveSnapshotDetectPornConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_snapshot_detect_porn_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_snapshot_detect_porn_config_with_options(request, runtime)

    def describe_live_snapshot_detect_porn_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse().from_map(self.do_request("DescribeLiveSnapshotDetectPornConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_snapshot_detect_porn_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_snapshot_detect_porn_config_with_options(request, runtime)

    def update_live_detect_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateLiveDetectNotifyConfigResponse().from_map(self.do_request("UpdateLiveDetectNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_live_detect_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_detect_notify_config_with_options(request, runtime)

    def update_live_snapshot_detect_porn_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse().from_map(self.do_request("UpdateLiveSnapshotDetectPornConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_live_snapshot_detect_porn_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_snapshot_detect_porn_config_with_options(request, runtime)

    def add_live_record_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveRecordNotifyConfigResponse().from_map(self.do_request("AddLiveRecordNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_record_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_record_notify_config_with_options(request, runtime)

    def delete_live_streams_notify_url_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse().from_map(self.do_request("DeleteLiveStreamsNotifyUrlConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_streams_notify_url_config_with_options(request, runtime)

    def delete_live_record_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveRecordNotifyConfigResponse().from_map(self.do_request("DeleteLiveRecordNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_record_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_notify_config_with_options(request, runtime)

    def describe_live_record_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveRecordNotifyConfigResponse().from_map(self.do_request("DescribeLiveRecordNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_record_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_record_notify_config_with_options(request, runtime)

    def describe_live_streams_notify_url_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse().from_map(self.do_request("DescribeLiveStreamsNotifyUrlConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_notify_url_config_with_options(request, runtime)

    def update_live_record_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateLiveRecordNotifyConfigResponse().from_map(self.do_request("UpdateLiveRecordNotifyConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_live_record_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_record_notify_config_with_options(request, runtime)

    def describe_live_streams_block_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamsBlockListResponse().from_map(self.do_request("DescribeLiveStreamsBlockList", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_streams_block_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_block_list_with_options(request, runtime)

    def describe_live_stream_online_user_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamOnlineUserNumResponse().from_map(self.do_request("DescribeLiveStreamOnlineUserNum", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_online_user_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_online_user_num_with_options(request, runtime)

    def describe_live_streams_publish_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamsPublishListResponse().from_map(self.do_request("DescribeLiveStreamsPublishList", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_streams_publish_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_publish_list_with_options(request, runtime)

    def describe_live_streams_online_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamsOnlineListResponse().from_map(self.do_request("DescribeLiveStreamsOnlineList", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_streams_online_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_online_list_with_options(request, runtime)

    def describe_live_streams_control_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamsControlHistoryResponse().from_map(self.do_request("DescribeLiveStreamsControlHistory", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_streams_control_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_control_history_with_options(request, runtime)

    def add_live_stream_transcode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveStreamTranscodeResponse().from_map(self.do_request("AddLiveStreamTranscode", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_stream_transcode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_stream_transcode_with_options(request, runtime)

    def delete_live_stream_transcode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveStreamTranscodeResponse().from_map(self.do_request("DeleteLiveStreamTranscode", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_stream_transcode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_transcode_with_options(request, runtime)

    def describe_live_streams_frame_rate_and_bit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamsFrameRateAndBitRateDataResponse().from_map(self.do_request("DescribeLiveStreamsFrameRateAndBitRateData", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_streams_frame_rate_and_bit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_frame_rate_and_bit_rate_data_with_options(request, runtime)

    def forbid_live_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ForbidLiveStreamResponse().from_map(self.do_request("ForbidLiveStream", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def forbid_live_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.forbid_live_stream_with_options(request, runtime)

    def describe_live_stream_transcode_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamTranscodeInfoResponse().from_map(self.do_request("DescribeLiveStreamTranscodeInfo", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_transcode_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_transcode_info_with_options(request, runtime)

    def set_live_streams_notify_url_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse().from_map(self.do_request("SetLiveStreamsNotifyUrlConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def set_live_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_streams_notify_url_config_with_options(request, runtime)

    def resume_live_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.ResumeLiveStreamResponse().from_map(self.do_request("ResumeLiveStream", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def resume_live_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_live_stream_with_options(request, runtime)

    def add_live_app_snapshot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveAppSnapshotConfigResponse().from_map(self.do_request("AddLiveAppSnapshotConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_app_snapshot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_app_snapshot_config_with_options(request, runtime)

    def add_live_app_record_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.AddLiveAppRecordConfigResponse().from_map(self.do_request("AddLiveAppRecordConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def add_live_app_record_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_app_record_config_with_options(request, runtime)

    def describe_live_record_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveRecordConfigResponse().from_map(self.do_request("DescribeLiveRecordConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_record_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_record_config_with_options(request, runtime)

    def delete_live_app_snapshot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveAppSnapshotConfigResponse().from_map(self.do_request("DeleteLiveAppSnapshotConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_app_snapshot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_app_snapshot_config_with_options(request, runtime)

    def delete_live_app_record_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DeleteLiveAppRecordConfigResponse().from_map(self.do_request("DeleteLiveAppRecordConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def delete_live_app_record_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_app_record_config_with_options(request, runtime)

    def create_live_stream_record_index_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.CreateLiveStreamRecordIndexFilesResponse().from_map(self.do_request("CreateLiveStreamRecordIndexFiles", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def create_live_stream_record_index_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_stream_record_index_files_with_options(request, runtime)

    def describe_live_stream_snapshot_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamSnapshotInfoResponse().from_map(self.do_request("DescribeLiveStreamSnapshotInfo", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_snapshot_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_snapshot_info_with_options(request, runtime)

    def describe_live_stream_record_index_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse().from_map(self.do_request("DescribeLiveStreamRecordIndexFiles", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_record_index_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_record_index_files_with_options(request, runtime)

    def describe_live_stream_record_index_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamRecordIndexFileResponse().from_map(self.do_request("DescribeLiveStreamRecordIndexFile", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_record_index_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_record_index_file_with_options(request, runtime)

    def describe_live_stream_record_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveStreamRecordContentResponse().from_map(self.do_request("DescribeLiveStreamRecordContent", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_stream_record_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_record_content_with_options(request, runtime)

    def describe_live_snapshot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.DescribeLiveSnapshotConfigResponse().from_map(self.do_request("DescribeLiveSnapshotConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def describe_live_snapshot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_snapshot_config_with_options(request, runtime)

    def update_live_app_snapshot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return live_20161101_models.UpdateLiveAppSnapshotConfigResponse().from_map(self.do_request("UpdateLiveAppSnapshotConfig", "HTTPS", "POST", "2016-11-01", "AK", None, request.to_map(), runtime))

    def update_live_app_snapshot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_app_snapshot_config_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
