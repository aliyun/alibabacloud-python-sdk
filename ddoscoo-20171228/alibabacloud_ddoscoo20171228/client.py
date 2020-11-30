# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_ddoscoo20171228 import models as ddoscoo_20171228_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddoscoo', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def modify_full_log_ttl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ModifyFullLogTtlResponse().from_map(self.do_request('ModifyFullLogTtl', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def modify_full_log_ttl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_full_log_ttl_with_options(request, runtime)

    def release_value_added_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ReleaseValueAddedResponse().from_map(self.do_request('ReleaseValueAdded', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def release_value_added(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_value_added_with_options(request, runtime)

    def list_value_added_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ListValueAddedResponse().from_map(self.do_request('ListValueAdded', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def list_value_added(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_value_added_with_options(request, runtime)

    def list_layer_7custom_ports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ListLayer7CustomPortsResponse().from_map(self.do_request('ListLayer7CustomPorts', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def list_layer_7custom_ports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_layer_7custom_ports_with_options(request, runtime)

    def describe_simple_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeSimpleDomainsResponse().from_map(self.do_request('DescribeSimpleDomains', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_simple_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_simple_domains_with_options(request, runtime)

    def describe_defense_count_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse().from_map(self.do_request('DescribeDefenseCountStatistics', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_defense_count_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_count_statistics_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.UntagResourcesResponse().from_map(self.do_request('UntagResources', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.TagResourcesResponse().from_map(self.do_request('TagResources', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ListTagResourcesResponse().from_map(self.do_request('ListTagResources', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ListTagKeysResponse().from_map(self.do_request('ListTagKeys', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def describe_domain_qps_with_cache_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse().from_map(self.do_request('DescribeDomainQpsWithCache', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_domain_qps_with_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_with_cache_with_options(request, runtime)

    def describe_log_store_exist_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse().from_map(self.do_request('DescribeLogStoreExistStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_log_store_exist_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_exist_status_with_options(request, runtime)

    def describe_batch_sls_dispatch_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse().from_map(self.do_request('DescribeBatchSlsDispatchStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_batch_sls_dispatch_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_sls_dispatch_status_with_options(request, runtime)

    def describe_sls_empty_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeSlsEmptyCountResponse().from_map(self.do_request('DescribeSlsEmptyCount', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_sls_empty_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_empty_count_with_options(request, runtime)

    def empty_sls_logstore_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.EmptySlsLogstoreResponse().from_map(self.do_request('EmptySlsLogstore', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def empty_sls_logstore(self, request):
        runtime = util_models.RuntimeOptions()
        return self.empty_sls_logstore_with_options(request, runtime)

    def close_domain_sls_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.CloseDomainSlsConfigResponse().from_map(self.do_request('CloseDomainSlsConfig', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def close_domain_sls_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_domain_sls_config_with_options(request, runtime)

    def open_domain_sls_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.OpenDomainSlsConfigResponse().from_map(self.do_request('OpenDomainSlsConfig', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def open_domain_sls_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_domain_sls_config_with_options(request, runtime)

    def describe_sls_logstore_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse().from_map(self.do_request('DescribeSlsLogstoreInfo', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_sls_logstore_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_logstore_info_with_options(request, runtime)

    def describe_sls_auth_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeSlsAuthStatusResponse().from_map(self.do_request('DescribeSlsAuthStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_sls_auth_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    def describe_sls_open_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeSlsOpenStatusResponse().from_map(self.do_request('DescribeSlsOpenStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_sls_open_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_open_status_with_options(request, runtime)

    def describe_domain_sls_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeDomainSlsStatusResponse().from_map(self.do_request('DescribeDomainSlsStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_domain_sls_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_sls_status_with_options(request, runtime)

    def config_domain_access_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ConfigDomainAccessModeResponse().from_map(self.do_request('ConfigDomainAccessMode', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def config_domain_access_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_domain_access_mode_with_options(request, runtime)

    def describe_domain_access_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeDomainAccessModeResponse().from_map(self.do_request('DescribeDomainAccessMode', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_domain_access_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_access_mode_with_options(request, runtime)

    def delete_async_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DeleteAsyncTaskResponse().from_map(self.do_request('DeleteAsyncTask', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_async_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_async_task_with_options(request, runtime)

    def create_async_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.CreateAsyncTaskResponse().from_map(self.do_request('CreateAsyncTask', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def create_async_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_async_task_with_options(request, runtime)

    def list_async_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ListAsyncTaskResponse().from_map(self.do_request('ListAsyncTask', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def list_async_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_async_task_with_options(request, runtime)

    def enable_layer_7ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.EnableLayer7CCRuleResponse().from_map(self.do_request('EnableLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def enable_layer_7ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_layer_7ccrule_with_options(request, runtime)

    def enable_layer_7ccwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.EnableLayer7CCResponse().from_map(self.do_request('EnableLayer7CC', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def enable_layer_7cc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_layer_7ccwith_options(request, runtime)

    def disable_layer_7ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DisableLayer7CCRuleResponse().from_map(self.do_request('DisableLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def disable_layer_7ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_layer_7ccrule_with_options(request, runtime)

    def disable_layer_7ccwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DisableLayer7CCResponse().from_map(self.do_request('DisableLayer7CC', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def disable_layer_7cc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_layer_7ccwith_options(request, runtime)

    def describle_layer_7instance_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse().from_map(self.do_request('DescribleLayer7InstanceRelations', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describle_layer_7instance_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describle_layer_7instance_relations_with_options(request, runtime)

    def describle_cert_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribleCertListResponse().from_map(self.do_request('DescribleCertList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describle_cert_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describle_cert_list_with_options(request, runtime)

    def describe_layer_7ccrules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeLayer7CCRulesResponse().from_map(self.do_request('DescribeLayer7CCRules', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_layer_7ccrules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_7ccrules_with_options(request, runtime)

    def describe_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeDomainsResponse().from_map(self.do_request('DescribeDomains', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    def describe_domain_qps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeDomainQpsResponse().from_map(self.do_request('DescribeDomainQps', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_domain_qps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_with_options(request, runtime)

    def describe_domain_attack_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeDomainAttackEventsResponse().from_map(self.do_request('DescribeDomainAttackEvents', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_domain_attack_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_attack_events_with_options(request, runtime)

    def describe_back_source_cidr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeBackSourceCidrResponse().from_map(self.do_request('DescribeBackSourceCidr', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_back_source_cidr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    def delete_layer_7rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DeleteLayer7RuleResponse().from_map(self.do_request('DeleteLayer7Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_layer_7rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_7rule_with_options(request, runtime)

    def delete_layer_7ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DeleteLayer7CCRuleResponse().from_map(self.do_request('DeleteLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_layer_7ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_7ccrule_with_options(request, runtime)

    def create_layer_7rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.CreateLayer7RuleResponse().from_map(self.do_request('CreateLayer7Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def create_layer_7rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_layer_7rule_with_options(request, runtime)

    def config_layer_7rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ConfigLayer7RuleResponse().from_map(self.do_request('ConfigLayer7Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def config_layer_7rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7rule_with_options(request, runtime)

    def config_layer_7cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ConfigLayer7CertResponse().from_map(self.do_request('ConfigLayer7Cert', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def config_layer_7cert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7cert_with_options(request, runtime)

    def config_layer_7cctemplate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse().from_map(self.do_request('ConfigLayer7CCTemplate', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def config_layer_7cctemplate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7cctemplate_with_options(request, runtime)

    def config_layer_7ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ConfigLayer7CCRuleResponse().from_map(self.do_request('ConfigLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def config_layer_7ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7ccrule_with_options(request, runtime)

    def config_layer_7black_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse().from_map(self.do_request('ConfigLayer7BlackWhiteList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def config_layer_7black_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7black_white_list_with_options(request, runtime)

    def add_layer_7ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.AddLayer7CCRuleResponse().from_map(self.do_request('AddLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def add_layer_7ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_layer_7ccrule_with_options(request, runtime)

    def release_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ReleaseInstanceResponse().from_map(self.do_request('ReleaseInstance', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def release_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    def modify_instance_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ModifyInstanceRemarkResponse().from_map(self.do_request('ModifyInstanceRemark', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def modify_instance_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_remark_with_options(request, runtime)

    def modify_elastic_band_width_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ModifyElasticBandWidthResponse().from_map(self.do_request('ModifyElasticBandWidth', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def modify_elastic_band_width(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_band_width_with_options(request, runtime)

    def describe_op_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeOpEntitiesResponse().from_map(self.do_request('DescribeOpEntities', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_op_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    def describe_layer_4rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeLayer4RulesResponse().from_map(self.do_request('DescribeLayer4Rules', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_layer_4rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rules_with_options(request, runtime)

    def describe_layer_4rule_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse().from_map(self.do_request('DescribeLayer4RuleAttributes', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_layer_4rule_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rule_attributes_with_options(request, runtime)

    def describe_ip_traffic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeIpTrafficResponse().from_map(self.do_request('DescribeIpTraffic', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_ip_traffic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_traffic_with_options(request, runtime)

    def describe_instance_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeInstanceStatisticsResponse().from_map(self.do_request('DescribeInstanceStatistics', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_instance_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    def describe_instance_specs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeInstanceSpecsResponse().from_map(self.do_request('DescribeInstanceSpecs', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_instance_specs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeInstancesResponse().from_map(self.do_request('DescribeInstances', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_instance_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeInstanceDetailsResponse().from_map(self.do_request('DescribeInstanceDetails', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_instance_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_details_with_options(request, runtime)

    def describe_health_check_status_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse().from_map(self.do_request('DescribeHealthCheckStatusList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_health_check_status_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_status_list_with_options(request, runtime)

    def describe_health_check_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeHealthCheckListResponse().from_map(self.do_request('DescribeHealthCheckList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_health_check_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_list_with_options(request, runtime)

    def describe_elastic_bandwidth_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse().from_map(self.do_request('DescribeElasticBandwidthSpec', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_elastic_bandwidth_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_bandwidth_spec_with_options(request, runtime)

    def describe_ddo_straffic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeDDoSTrafficResponse().from_map(self.do_request('DescribeDDoSTraffic', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_ddo_straffic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_straffic_with_options(request, runtime)

    def describe_ddo_sevents_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DescribeDDoSEventsResponse().from_map(self.do_request('DescribeDDoSEvents', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_ddo_sevents(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_sevents_with_options(request, runtime)

    def delete_layer_4rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.DeleteLayer4RuleResponse().from_map(self.do_request('DeleteLayer4Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_layer_4rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_4rule_with_options(request, runtime)

    def create_layer_4rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.CreateLayer4RuleResponse().from_map(self.do_request('CreateLayer4Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def create_layer_4rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_layer_4rule_with_options(request, runtime)

    def config_layer_4rule_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse().from_map(self.do_request('ConfigLayer4RuleAttribute', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def config_layer_4rule_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_attribute_with_options(request, runtime)

    def config_layer_4rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ConfigLayer4RuleResponse().from_map(self.do_request('ConfigLayer4Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def config_layer_4rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_with_options(request, runtime)

    def config_health_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddoscoo_20171228_models.ConfigHealthCheckResponse().from_map(self.do_request('ConfigHealthCheck', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime))

    def config_health_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_health_check_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
