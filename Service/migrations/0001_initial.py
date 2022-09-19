# Generated by Django 3.2.13 on 2022-09-04 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AspirantData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=40)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utme', models.IntegerField()),
                ('putme', models.IntegerField()),
                ('department', models.CharField(choices=[('Faculty of Arts', (('Anthroplogy', 'Anthroplogy'), ('Arabic Language and Literature', 'Arabic Language and Literature'), ('Archaeology', 'Archaeology'), ('Classics', 'Classics'), ('Communication and Language Arts', 'Communication and Language Arts'), ('English Language and Literature', 'English Language and Literature'), ('European Studies French', 'European Studies French'), ('European Studies German', 'European Studies German'), ('European Studies Russian', 'European Studies Russian'), ('History', 'History'), ('Islamic Studies', 'Islamic Studies'), ('Linguistic', 'Linguistic'), ('Linguistic Igbo', 'Linguistic Igbo'), ('Linguistic Yoruba', 'Linguistic Yoruba'), ('Music', 'Music'), ('Philosophy', 'Philosophy'), ('Religious Studies', 'Religious Studies'), ('Theartre Arts', 'Theartre Arts'))), ('Faculty of Agriculture', (('Agricultural Extension', 'Agricultural Extension'), ('Agronomy', 'Agronomy'))), ('College of Medicine', (('Biochemistry', 'Biochemistry'), ('Dentistry', 'Dentistry'), ('Environmental Health Science', 'Environmental Health Science'), ('Human Nutrition', 'Human Nutrition'), ('Medical Laboratory Science', 'Medical Laboratory Science'), ('Medicine and Surgery', 'Medicine and Surgery'), ('Nursing Science', 'Nursing Science'), ('Physiology', 'Physiology'), ('Physiotherapy', 'Physiotherapy'))), ('Faculty of Education', (('Adult Education', 'Adult Education'), ('Arabic Studies Education', 'Arabic Studies Education'), ('Biology Education', 'Biology Education'), ('Chemistry Education', 'Chemistry Education'), ('Christian Religious Studies Education', 'Christian Religious Studies Education'), ('Communication and Language Arts Education', 'Communication and Language Arts Education'), ('Early Childhood Education', 'Early Childhood Education'), ('Economics Education', 'Economics Education'), ('Educational Management', 'Educational Management'), ('English Education', 'English Education'), ('French Education', 'French Education'), ('Geography Education', 'Geography Education'), ('Guidance and Counselling', 'Guidance and Counselling'), ('Health Education', 'Health Education'), ('History Education', 'History Education'), ('Human Kinetics', 'Human Kinetics'), ('Islamic Studies Education', 'Islamic Studies Education'), ('LARIS', 'LARIS'), ('Mathematics Education', 'Mathematics Education'), ('Physics Education', 'Physics Education'), ('Political Science Education', 'Political Science Education'), ('Education and Religious Studies', 'Education and Religious Studies'), ('Special Education', 'Special Education'), ('Yoruba Education', 'Yoruba Education'))), ('Faculty of Economics', (('Economics', 'Economics'),)), ('Faculty of Law', (('Law', 'Law'),)), ('Faculty of Pharmacy', (('Pharmacy', 'Pharmacy'),)), ('Faculty of Veterinary Medicine', (('Veterinary Medicine', 'Veterinary Medicine'),)), ('Faculty of Environment and Design', (('Architecture', 'Architecture'), ('Estate Management', 'Estate Management'), ('Urban and Regional Planning', 'Urban and Regional Planning'))), ('Faculty of Science', (('Geography', 'Geography'), ('Political Science', 'Political Science'), ('Psychology', 'Psychology'), ('Sociology', 'Sociology'))), ('Faculty of Engineering', (('Agricultural & Environmental Engineering', 'Agricultural & Environmental Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'), ('Food Technology', 'Food Technology'), ('Industrial and Production Engineering', 'Industrial and Production Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Petroleum Engineering', 'Petroleum Engineering'), ('Wood Products Engineering', 'Wood Products Engineering'))), ('Faculty of Science', (('Anthropology', 'Anthropology'), ('Archaeology', 'Archaeology'), ('Botany', 'Botany'), ('Chemistry', 'Chemistry'), ('Computer Science', 'Computer Science'), ('Geography', 'Geography'), ('Geology', 'Geology'), ('Industrial Chemistry', 'Industrial Chemistry'), ('Mathematics', 'Mathematics'), ('Microbiology', 'Microbiology'), ('Physics', 'Physics'), ('Statistics', 'Statistics'), ('Zoology', 'Zoology'))), ('Faculty of Renewable and Natural Resources', (('Aquaculture and Fisheries Management', 'Aquaculture and Fisheries Management'), ('Forest Resource Management', 'Forest Resource Management'), ('Social and Environmental Forestry', 'Social and Environmental Forestry'), ('Wildlife and Ecotourism Management', 'Wildlife and Ecotourism Management')))], max_length=50)),
                ('year_of_admission', models.IntegerField()),
                ('number_of_attempts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Faculty of Arts', (('Anthroplogy', 'Anthroplogy'), ('Arabic Language and Literature', 'Arabic Language and Literature'), ('Archaeology', 'Archaeology'), ('Classics', 'Classics'), ('Communication and Language Arts', 'Communication and Language Arts'), ('English Language and Literature', 'English Language and Literature'), ('European Studies French', 'European Studies French'), ('European Studies German', 'European Studies German'), ('European Studies Russian', 'European Studies Russian'), ('History', 'History'), ('Islamic Studies', 'Islamic Studies'), ('Linguistic', 'Linguistic'), ('Linguistic Igbo', 'Linguistic Igbo'), ('Linguistic Yoruba', 'Linguistic Yoruba'), ('Music', 'Music'), ('Philosophy', 'Philosophy'), ('Religious Studies', 'Religious Studies'), ('Theartre Arts', 'Theartre Arts'))), ('Faculty of Agriculture', (('Agricultural Extension', 'Agricultural Extension'), ('Agronomy', 'Agronomy'))), ('College of Medicine', (('Biochemistry', 'Biochemistry'), ('Dentistry', 'Dentistry'), ('Environmental Health Science', 'Environmental Health Science'), ('Human Nutrition', 'Human Nutrition'), ('Medical Laboratory Science', 'Medical Laboratory Science'), ('Medicine and Surgery', 'Medicine and Surgery'), ('Nursing Science', 'Nursing Science'), ('Physiology', 'Physiology'), ('Physiotherapy', 'Physiotherapy'))), ('Faculty of Education', (('Adult Education', 'Adult Education'), ('Arabic Studies Education', 'Arabic Studies Education'), ('Biology Education', 'Biology Education'), ('Chemistry Education', 'Chemistry Education'), ('Christian Religious Studies Education', 'Christian Religious Studies Education'), ('Communication and Language Arts Education', 'Communication and Language Arts Education'), ('Early Childhood Education', 'Early Childhood Education'), ('Economics Education', 'Economics Education'), ('Educational Management', 'Educational Management'), ('English Education', 'English Education'), ('French Education', 'French Education'), ('Geography Education', 'Geography Education'), ('Guidance and Counselling', 'Guidance and Counselling'), ('Health Education', 'Health Education'), ('History Education', 'History Education'), ('Human Kinetics', 'Human Kinetics'), ('Islamic Studies Education', 'Islamic Studies Education'), ('LARIS', 'LARIS'), ('Mathematics Education', 'Mathematics Education'), ('Physics Education', 'Physics Education'), ('Political Science Education', 'Political Science Education'), ('Education and Religious Studies', 'Education and Religious Studies'), ('Special Education', 'Special Education'), ('Yoruba Education', 'Yoruba Education'))), ('Faculty of Economics', (('Economics', 'Economics'),)), ('Faculty of Law', (('Law', 'Law'),)), ('Faculty of Pharmacy', (('Pharmacy', 'Pharmacy'),)), ('Faculty of Veterinary Medicine', (('Veterinary Medicine', 'Veterinary Medicine'),)), ('Faculty of Environment and Design', (('Architecture', 'Architecture'), ('Estate Management', 'Estate Management'), ('Urban and Regional Planning', 'Urban and Regional Planning'))), ('Faculty of Science', (('Geography', 'Geography'), ('Political Science', 'Political Science'), ('Psychology', 'Psychology'), ('Sociology', 'Sociology'))), ('Faculty of Engineering', (('Agricultural & Environmental Engineering', 'Agricultural & Environmental Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'), ('Food Technology', 'Food Technology'), ('Industrial and Production Engineering', 'Industrial and Production Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Petroleum Engineering', 'Petroleum Engineering'), ('Wood Products Engineering', 'Wood Products Engineering'))), ('Faculty of Science', (('Anthropology', 'Anthropology'), ('Archaeology', 'Archaeology'), ('Botany', 'Botany'), ('Chemistry', 'Chemistry'), ('Computer Science', 'Computer Science'), ('Geography', 'Geography'), ('Geology', 'Geology'), ('Industrial Chemistry', 'Industrial Chemistry'), ('Mathematics', 'Mathematics'), ('Microbiology', 'Microbiology'), ('Physics', 'Physics'), ('Statistics', 'Statistics'), ('Zoology', 'Zoology'))), ('Faculty of Renewable and Natural Resources', (('Aquaculture and Fisheries Management', 'Aquaculture and Fisheries Management'), ('Forest Resource Management', 'Forest Resource Management'), ('Social and Environmental Forestry', 'Social and Environmental Forestry'), ('Wildlife and Ecotourism Management', 'Wildlife and Ecotourism Management')))], max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='services/')),
                ('text', models.TextField()),
                ('url', models.CharField(max_length=25)),
                ('number', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('Accounts', 'Accounts'), ('Arabic Studies', 'Arabic Studies'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Commerce', 'Commerce'), ('CRS', 'CRS'), ('Economics', 'Economics'), ('Fine and Applied Arts', 'Fine and Applied Arts'), ('French', 'French'), ('Geography', 'Geography'), ('Government', 'Government'), ('Hausa', 'Hausa'), ('History', 'History'), ('Home Economics', 'Home Economics'), ('Igbo Language', 'Igbo Language'), ('Islamic Studies', 'Islamic studies'), ('Literature in English', 'Literature in English'), ('Mathematics', 'Mathematics'), ('Music', 'Music'), ('Physics', 'Physics'), ('Use of English', 'Use of English'), ('Yoruba Language', 'Yoruba Language')], max_length=30)),
                ('is_verified', models.BooleanField(default=False, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_combo', to='Service.department')),
            ],
        ),
        migrations.CreateModel(
            name='CutOff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.FloatField(blank=True, null=True)),
                ('competitiveness', models.IntegerField(blank=True, null=True)),
                ('quota', models.IntegerField(blank=True, null=True)),
                ('cutoff_2016', models.FloatField(blank=True, null=True)),
                ('cutoff_2017', models.FloatField(blank=True, null=True)),
                ('cutoff_2018', models.FloatField(blank=True, null=True)),
                ('cutoff_2019', models.FloatField(blank=True, null=True)),
                ('cutoff_2021', models.FloatField(blank=True, null=True)),
                ('predicted', models.FloatField(null=True)),
                ('mean', models.FloatField(blank=True, null=True)),
                ('next_prediction', models.FloatField(blank=True, null=True)),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cutoff', to='Service.department')),
            ],
        ),
    ]
