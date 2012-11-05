from django.conf.urls.defaults import patterns  # , include, url

urlpatterns = patterns(
    'freezers.views',
    (r'^$', 'freezer_index'),
    (r'^new/$', 'add_freezer'),
    (r'^(?P<freezer_id>\d+)/select-location/$', 'select_sample_location'),
    (r'^(?P<freezer_id>\d+)/select-sample-location/$',
        'select_sample_location'),
    (r'^(?P<freezer_id>\d+)/(?P<address>\d+)/$', 'show_box'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/$',
        'select_box_location'),
    (r'^(?P<freezer_id>\d+)/add-samples/$', 'add_samples_to_freezer'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/add-samples/$',
        'add_samples_to_freezer'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/add-samples/$',
        'add_samples_to_freezer'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/add-samples/$',
        'add_samples_to_freezer'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/(?P<cell_id>\d+)/add-samples/$',
        'add_samples_to_freezer'),
    (r'^(?P<freezer_id>\d+)/samples/$', 'sample_index_by_location'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/samples/$',
     'sample_index_by_location'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/samples/$',
     'sample_index_by_location'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/samples/$',
        'sample_index_by_location'),
    (r'^samples/$', 'sample_index'),
    (r'^suppliers/new/$', 'add_supplier'),
    (r'^suppliers/$', 'supplier_index'),
    (r'^sample-type/new/$', 'add_sample_type'),
    (r'^(?P<freezer_id>\d+)/$', 'freezer_detail'),
    (r'^suppliers/(?P<supplier_id>\d+)/$', 'supplier_detail'),
    (r'^samples/(?P<sample_id>\d+)/$', 'sample_detail'),
    (r'^(?P<freezer_id>\d+)/edit/$', 'edit_freezer'),
    (r'^(?P<freezer_id>\d+)/remove/$', 'remove_freezer'),
    (r'^suppliers/(?P<supplier_id>\d+)/edit/$', 'edit_supplier'),
    (r'^samples/(?P<sample_id>\d+)/edit/$', 'edit_sample'),
    (r'^samples/(?P<sample_id>\d+)/move/$', 'move_sample_select_freezer'),
    (r'^samples/(?P<sample_id>\d+)/(?P<freezer_id>\d+)/move/(?P<atoa>\d+)/$',
        'move_sample'),
    (r'^samples/(?P<sample_id>\d+)/(?P<freezer_id>\d+)/move/(?P<atoa>\d+)/$',
        'move_sample'),
    (r'^samples/(?P<sample_id>\d+)/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/move/(?P<atoa>\d+)/$',
        'move_sample'),
    (r'^samples/(?P<sample_id>\d+)/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/move/(?P<atoa>\d+)/$',
        'move_sample'),
    (r'^samples/(?P<sample_id>\d+)/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/move/(?P<atoa>\d+)/$',
        'move_sample'),
    (r'^samples/(?P<sample_id>\d+)/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/move/(?P<atoa>\d+)/$',
        'move_sample'),
    (r'^samples/(?P<sample_id>\d+)/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/(?P<cell_id>\d+)/move/(?P<atoa>\d+)/$',
        'move_sample'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/move-box/$',
        'move_box_select_freezer'),
    (r'(?P<box_address>\d+)/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/move-box/$',
        'move_box'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/rearrange-samples/$',
        'rearrange_samples_within_box'),
    (r'^samples/(?P<sample_id>\d+)/(?P<cell_id>\d+)/swap-samples/$', 'swap_samples'),
    (r'^samples/(?P<sample_id>\d+)/remove/$', 'remove_sample_from_index'),
    (r'^samples/(?P<sample_id>\d+)/remove-sample/$', 'remove_sample'),
    (r'^search/$', 'search'),
    (r'^(?P<freezer_id>\d+)/select-region-to-edit/$',
        'select_region_to_edit'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/edit-region/$',
        'edit_freezer_region'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/edit-region/$',
        'edit_freezer_region'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/edit-region/$',
        'edit_freezer_region'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/edit-region/$',
        'edit_freezer_region'),
    (r'^removed/((?P<query>[^/]+)/)?$', 'removed_index'),
    (r'^removed/(?P<removed_id>\d+)/detail/$', 'removed_detail'),
    (r'^removed/(?P<removed_id>\d+)/return/$', 'return_removed_sample'),
    (r'^home/$', 'home_link'),
    (r'^home/(?P<user_id>\d+)/$', 'homepage'),
    (r'^messages/(?P<msg_id>\d+)/delete/$', 'delete_message'),
    (r'^messages/(?P<msg_id>\d+)/reply/$', 'reply_to_message'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/select-samples/$',
        'select_samples_in_box'),
    (r'^move-selected/$',
        'move_selected_samples_select_freezer'),
    (r'^move-selected/(?P<freezer_id>\d+)/$',
        'move_selection'),
    (r'^move-selected/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/$',
        'move_selection'),
    (r'^move-selected/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/$',
        'move_selection'),
    (r'^move-selected/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/$',
        'move_selection'),
    (r'^move-selected/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/$',
        'move_selection'),
    (r'^move-selected/(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/(?P<cell_id>\d+)/$',
        'move_selection'),
    (r'^remove-selected-samples/$', 'remove_selected_samples'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/remodel/$',
        'remodel_freezer'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/remodel/$',
        'remodel_freezer'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/remodel/$',
        'remodel_freezer'),
    (r'^(?P<freezer_id>\d+)/(?P<shelf_id>\d+)/(?P<rack_id>\d+)/(?P<drawer_id>\d+)/(?P<box_id>\d+)/remodel/$',
        'remodel_freezer'),
    (r'^export-samples/$', 'export_samples'),
    (r'^delete-file/(?P<file_id>\d+)/$', 'delete_file'),
    (r'^(?P<freezer_id>\d+)/(?P<addr>\d+)/name-box/$', 'name_box'),
)
