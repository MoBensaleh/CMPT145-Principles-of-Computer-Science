import llist_integration_test as integration

all_of_em = [
    integration.test_integration_add_to_back_is_empty,
    integration.test_integration_add_to_back_size,
    integration.test_integration_add_to_back_value_is_in,
    integration.test_integration_add_to_back_value_is_in_2,
    integration.test_integration_add_to_back_value_is_in_3,
    integration.test_integration_add_to_back_value_is_in_4,
    integration.test_integration_add_to_back_get_index_of_value_1,
    integration.test_integration_add_to_back_get_index_of_value_2,
    integration.test_integration_add_to_back_get_index_of_value_3,
    integration.test_integration_add_to_back_get_index_of_value_4,
    integration.test_integration_add_to_back_retrieve_data_at_index_1,
    integration.test_integration_add_to_back_retrieve_data_at_index_2,
    integration.test_integration_add_to_back_retrieve_data_at_index_3,
    integration.test_integration_add_to_back_retrieve_data_at_index_4,
    integration.test_integration_add_to_front_is_empty,
    integration.test_integration_add_to_front_size,
    integration.test_integration_add_to_front_value_is_in_1,
    integration.test_integration_add_to_front_value_is_in_2,
    integration.test_integration_add_to_front_value_is_in_3,
    integration.test_integration_add_to_front_value_is_in_4,
    integration.test_integration_add_to_front_get_index_of_value_1,
    integration.test_integration_add_to_front_get_index_of_value_2,
    integration.test_integration_add_to_front_get_index_of_value_3,
    integration.test_integration_add_to_front_get_index_of_value_4,
    integration.test_integration_add_to_front_retrieve_data_at_index_1,
    integration.test_integration_add_to_front_retrieve_data_at_index_2,
    integration.test_integration_add_to_front_retrieve_data_at_index_3,
    integration.test_integration_add_to_front_retrieve_data_at_index_4,
    integration.test_integration_set_data_check_1,
    integration.test_integration_set_data_get_index_of_value_1,
    integration.test_integration_set_data_get_index_of_value_2,
    integration.test_integration_set_data_get_index_of_value_3,
    integration.test_integration_set_data_get_index_of_value_4,
    integration.test_integration_set_data_size_1,
    integration.test_integration_set_data_get_index_of_check_2,
    integration.test_integration_set_data_get_index_of_value_5,
    integration.test_integration_set_data_get_index_of_value_6,
    integration.test_integration_set_data_get_index_of_value_7,
    integration.test_integration_set_data_get_index_of_value_8,
    integration.test_integration_set_data_get_index_of_size_2,
    integration.test_integration_set_data_get_index_of_check_3,
    integration.test_integration_set_data_get_index_of_value_9,
    integration.test_integration_set_data_get_index_of_value_10,
    integration.test_integration_set_data_get_index_of_size_3,
    integration.test_integration_insert_value_at_index_check_1,
    integration.test_integration_insert_value_at_index_get_index_of_value_1,
    integration.test_integration_insert_value_at_index_get_index_of_value_2,
    integration.test_integration_insert_value_at_index_size_1,
    integration.test_integration_insert_value_at_index_check_2,
    integration.test_integration_insert_value_at_index_get_index_of_value_3,
    integration.test_integration_insert_value_at_index_get_index_of_value_4,
    integration.test_integration_insert_value_at_index_size_2,
    integration.test_integration_insert_value_at_index_check_3,
    integration.test_integration_insert_value_at_index_get_index_of_value_5,
    integration.test_integration_insert_value_at_index_get_index_of_value_6,
    integration.test_integration_insert_value_at_index_size_4,
    integration.test_integration_delete_item_at_index_check_1,
    integration.test_integration_delete_item_at_index_get_index_of_value_1,
    integration.test_integration_delete_item_at_index_value_is_in_1,
    integration.test_integration_delete_item_at_index_size_1,
    integration.test_integration_delete_item_at_index_get_index_of_value_2,
    integration.test_integration_delete_item_at_index_check_2,
    integration.test_integration_delete_item_at_index_get_index_of_value_3,
    integration.test_integration_delete_item_at_index_value_is_in_2,
    integration.test_integration_delete_item_at_index_size_2,
    integration.test_integration_delete_item_at_index_get_index_of_value_4,
    integration.test_integration_delete_item_at_index_check_3,
    integration.test_integration_delete_item_at_index_get_index_of_value_5,
    integration.test_integration_delete_item_at_index_value_is_in_3,
    integration.test_integration_delete_item_at_index_size_3,
    integration.test_integration_delete_item_at_index_get_index_of_value_6,
    integration.test_integration_remove_from_back_size,
    integration.test_integration_remove_from_back_get_index_of_value_1,
    integration.test_integration_remove_from_back_get_index_of_value_2,
    integration.test_integration_remove_from_back_retrieve_data_at_index_1,
    integration.test_integration_remove_from_front_size,
    integration.test_integration_remove_from_front_get_index_of_value_1,
    integration.test_integration_remove_from_front_get_index_of_value_2,
    integration.test_integration_remove_from_front_retrieve_data_at_index_1
    ]

count = 0
failed = 0
for t in all_of_em:
    count += 1
    try:
        t()
    except Exception as e:
        print("Test failure in function:", t.__name__)
        print(e)
        print()
        failed += 1

print('Passed', count - failed, 'out of total', count, 'tests')

