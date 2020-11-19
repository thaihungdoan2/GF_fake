# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounttable(models.Model):
    codifid = models.IntegerField(primary_key=True)
    type = models.SmallIntegerField()
    owner = models.IntegerField(blank=True, null=True)
    acgroup = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'accounttable'


class AgLitter(models.Model):
    litter_id = models.IntegerField(primary_key=True)
    beginlitdate = models.DateField()
    fosteron = models.IntegerField()
    fosteroff = models.IntegerField()
    deaths = models.IntegerField()
    totalwean = models.IntegerField()
    weandate = models.DateField(blank=True, null=True)
    iid_parity = models.ForeignKey('AgParity', models.DO_NOTHING, db_column='iid_parity', blank=True, null=True)
    fk_wean_event = models.IntegerField(blank=True, null=True)
    fk_begin_event = models.IntegerField(blank=True, null=True)
    herd = models.ForeignKey('Herd', models.DO_NOTHING)
    weanlocation = models.CharField(max_length=10, blank=True, null=True)
    weanloc1 = models.CharField(max_length=10, blank=True, null=True)
    weanloc2 = models.CharField(max_length=10, blank=True, null=True)
    nurseonage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ag_litter'

    def __str__(self):
        return self.litter_id

class AgMilklac(models.Model):
    parity = models.ForeignKey('AgParity', models.DO_NOTHING)
    herd = models.ForeignKey('Herd', models.DO_NOTHING)
    mlmilk = models.FloatField(blank=True, null=True)
    mlfat = models.FloatField(blank=True, null=True)
    mlprot = models.FloatField(blank=True, null=True)
    mlscc = models.FloatField(blank=True, null=True)
    mlmun = models.FloatField(blank=True, null=True)
    mlsnf = models.FloatField(blank=True, null=True)
    mpmilk = models.FloatField(blank=True, null=True)
    mpfat = models.FloatField(blank=True, null=True)
    mpprot = models.FloatField(blank=True, null=True)
    mpscc = models.FloatField(blank=True, null=True)
    mpmun = models.FloatField(blank=True, null=True)
    mpsnf = models.FloatField(blank=True, null=True)
    mfmilk = models.FloatField(blank=True, null=True)
    mffat = models.FloatField(blank=True, null=True)
    mfprot = models.FloatField(blank=True, null=True)
    mfscc = models.FloatField(blank=True, null=True)
    mfmun = models.FloatField(blank=True, null=True)
    mfsnf = models.FloatField(blank=True, null=True)
    ntests = models.SmallIntegerField()
    lacdim = models.SmallIntegerField(blank=True, null=True)
    milkpeak = models.FloatField(blank=True, null=True)
    dimpeak = models.FloatField(blank=True, null=True)
    sumlacdim = models.IntegerField(blank=True, null=True)
    mldays = models.IntegerField(blank=True, null=True)
    dlmilk = models.FloatField(blank=True, null=True)
    dfmilk = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ag_milklac'


class AgMilkmeter(models.Model):
    mm_id = models.IntegerField(primary_key=True)
    herd = models.ForeignKey('Herd', models.DO_NOTHING)
    milklac = models.ForeignKey('AgParity', models.DO_NOTHING, blank=True, null=True)
    mmdate = models.DateField()
    weight = models.FloatField()
    time = models.TimeField(blank=True, null=True)
    peakflow = models.FloatField(blank=True, null=True)
    milkduration = models.FloatField(blank=True, null=True)
    scc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ag_milkmeter'


class AgParity(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    herd = models.ForeignKey('Herd', models.DO_NOTHING)
    litterid = models.CharField(max_length=10, blank=True, null=True)
    iid_nextparity = models.IntegerField(blank=True, null=True)
    iid_prevparity = models.IntegerField(blank=True, null=True)
    iid_lstservice = models.IntegerField(blank=True, null=True)
    birthingdate = models.DateField(blank=True, null=True)
    endparitydate = models.DateField(blank=True, null=True)
    birthingint = models.SmallIntegerField(blank=True, null=True)
    conceptdate = models.DateField(blank=True, null=True)
    fosteron = models.SmallIntegerField(blank=True, null=True)
    fosteroff = models.SmallIntegerField(blank=True, null=True)
    fstservdate = models.DateField(blank=True, null=True)
    groupid = models.CharField(max_length=3, blank=True, null=True)
    liveborn = models.SmallIntegerField(blank=True, null=True)
    mummies = models.SmallIntegerField(blank=True, null=True)
    parity = models.SmallIntegerField(blank=True, null=True)
    recordedpwdeaths = models.SmallIntegerField(blank=True, null=True)
    stillborn = models.SmallIntegerField(blank=True, null=True)
    lweandate = models.DateField(blank=True, null=True)
    wean1date = models.DateField(blank=True, null=True)
    wean1num = models.SmallIntegerField(blank=True, null=True)
    totalweaned = models.SmallIntegerField(blank=True, null=True)
    littersweaned = models.SmallIntegerField(blank=True, null=True)
    nservices = models.SmallIntegerField(blank=True, null=True)
    lnurseondate = models.DateField(blank=True, null=True)
    nurseon = models.SmallIntegerField(blank=True, null=True)
    birthloc1 = models.CharField(max_length=10, blank=True, null=True)
    birthloc2 = models.CharField(max_length=10, blank=True, null=True)
    birthlocation = models.CharField(max_length=10, blank=True, null=True)
    sumweanweight = models.FloatField(blank=True, null=True)
    countweanweight = models.SmallIntegerField(blank=True, null=True)
    sumweanage = models.IntegerField(blank=True, null=True)
    countweanage = models.SmallIntegerField(blank=True, null=True)
    nurseoff = models.SmallIntegerField(blank=True, null=True)
    sumadjweanweight = models.FloatField(blank=True, null=True)
    countadjweanweight = models.SmallIntegerField(blank=True, null=True)
    birthweight = models.FloatField(blank=True, null=True)
    abortions = models.SmallIntegerField(blank=True, null=True)
    maleborn = models.SmallIntegerField(blank=True, null=True)
    malestillborn = models.SmallIntegerField(blank=True, null=True)
    sumnurseages = models.SmallIntegerField(blank=True, null=True)
    countnurseages = models.SmallIntegerField(blank=True, null=True)
    lstbirthdatelitter = models.DateField(blank=True, null=True)
    iid_conceptservice = models.IntegerField(blank=True, null=True)
    endlacdate = models.DateField(blank=True, null=True)
    paritypos = models.SmallIntegerField(blank=True, null=True)
    adjliveborn = models.FloatField(blank=True, null=True)
    cgliveborn = models.FloatField(blank=True, null=True)
    cgweanweight = models.FloatField(blank=True, null=True)
    lstcomment = models.CharField(max_length=30, blank=True, null=True)
    iid_lsttreatment = models.IntegerField(blank=True, null=True)
    prevendlacfstserv = models.SmallIntegerField(blank=True, null=True)
    prevlactationlen = models.SmallIntegerField(blank=True, null=True)
    prevendlacdate = models.DateField(blank=True, null=True)
    birthingproblem = models.IntegerField(blank=True, null=True)
    induced = models.IntegerField(blank=True, null=True)
    paritylabel = models.CharField(max_length=40, blank=True, null=True)
    feedin = models.FloatField(blank=True, null=True)
    lactationfeedin = models.FloatField(blank=True, null=True)
    iid_fstservice = models.IntegerField(blank=True, null=True)
    fsthnsdate = models.DateField(blank=True, null=True)
    weanfstserv = models.SmallIntegerField(blank=True, null=True)
    nhns = models.SmallIntegerField(blank=True, null=True)
    isindividualbirthweight = models.SmallIntegerField(blank=True, null=True)
    birthweightcount = models.SmallIntegerField(blank=True, null=True)
    iid_birthuserfields = models.IntegerField(blank=True, null=True)
    iid_lstlitter = models.IntegerField(blank=True, null=True)
    birthingtech = models.IntegerField(blank=True, null=True)
    beginactiveparitydate = models.DateField(blank=True, null=True)
    outfarm = models.SmallIntegerField()
    fstheattreatdate = models.DateField(blank=True, null=True)
    sumweanages = models.SmallIntegerField(blank=True, null=True)
    countweanages = models.SmallIntegerField(blank=True, null=True)
    birthingcomment = models.CharField(max_length=255, blank=True, null=True)
    fstconceptdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ag_parity'

    def __str__(self):
        return self.id

class AgServices(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    herd = models.ForeignKey('Herd', models.DO_NOTHING)
    iid_parity = models.IntegerField()
    iid_nextparity = models.IntegerField(blank=True, null=True)
    servdate = models.DateField()
    servresultdays = models.SmallIntegerField(blank=True, null=True)
    servhour1 = models.SmallIntegerField(blank=True, null=True)
    servhour2 = models.SmallIntegerField(blank=True, null=True)
    servhour3 = models.SmallIntegerField(blank=True, null=True)
    servmale = models.CharField(max_length=10, blank=True, null=True)
    servmale1 = models.CharField(max_length=10, blank=True, null=True)
    servmale2 = models.CharField(max_length=10, blank=True, null=True)
    servmale3 = models.CharField(max_length=10, blank=True, null=True)
    servtype = models.CharField(max_length=1, blank=True, null=True)
    matings = models.SmallIntegerField(blank=True, null=True)
    nservice = models.SmallIntegerField(blank=True, null=True)
    pregdiagresult = models.SmallIntegerField(blank=True, null=True)
    parity = models.SmallIntegerField(blank=True, null=True)
    servgroupid = models.CharField(max_length=4, blank=True, null=True)
    pregdiagdate = models.DateField(blank=True, null=True)
    servresult = models.SmallIntegerField(blank=True, null=True)
    priorservint = models.SmallIntegerField(blank=True, null=True)
    priorservresult = models.SmallIntegerField(blank=True, null=True)
    servmalegenetics = models.IntegerField(blank=True, null=True)
    servtech = models.IntegerField(blank=True, null=True)
    servtech1 = models.IntegerField(blank=True, null=True)
    servtech2 = models.IntegerField(blank=True, null=True)
    servtech3 = models.IntegerField(blank=True, null=True)
    gestlocation = models.CharField(max_length=10, blank=True, null=True)
    gestloc1 = models.CharField(max_length=10, blank=True, null=True)
    gestloc2 = models.CharField(max_length=10, blank=True, null=True)
    lstservuserfieldid = models.IntegerField(blank=True, null=True)
    iid_lsttreatment = models.IntegerField(blank=True, null=True)
    iid_prevservice = models.IntegerField(blank=True, null=True)
    iid_lsthns = models.IntegerField(blank=True, null=True)
    outfarm = models.SmallIntegerField()
    iid_servmating1 = models.IntegerField(blank=True, null=True)
    iid_servmating2 = models.IntegerField(blank=True, null=True)
    iid_servmating3 = models.IntegerField(blank=True, null=True)
    iid_nextservice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ag_services'


class Codiftable(models.Model):
    codifid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True, null=True)
    codiftype = models.SmallIntegerField()
    isactive = models.CharField(max_length=1)
    code = models.CharField(max_length=10, blank=True, null=True)
    int0 = models.IntegerField(blank=True, null=True)
    inventoryid = models.IntegerField(blank=True, null=True)
    label = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codiftable'
        unique_together = (('codiftype', 'name'),)


class Dblog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    logdate = models.DateTimeField()
    dataver = models.IntegerField(blank=True, null=True)
    logtype = models.IntegerField()
    data = models.CharField(max_length=300, blank=True, null=True)
    refid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dblog'


class Dmbreeding(models.Model):
    id = models.BigIntegerField(primary_key=True)
    period = models.CharField(max_length=10)
    parity = models.IntegerField()
    genetics = models.CharField(max_length=30, blank=True, null=True)
    nweaned = models.IntegerField()
    livebornlitweaned = models.IntegerField()
    netfostered = models.IntegerField()
    abortions = models.IntegerField()
    p0abortions = models.IntegerField()
    recordedpwdeaths = models.IntegerField()
    transferredout = models.IntegerField()
    culled = models.IntegerField()
    deaths = models.IntegerField()
    removed = models.IntegerField()
    sumparityculled = models.IntegerField()
    lfliveborn = models.IntegerField()
    lftotalweaned = models.IntegerField()
    heatnotserved = models.IntegerField()
    hnsunmated = models.IntegerField()
    nurseoff = models.IntegerField()
    nurseon = models.IntegerField()
    totalweaned = models.IntegerField()
    littersweaned = models.IntegerField()
    naturaltotalweaned = models.IntegerField()
    naturallittersweaned = models.IntegerField()
    countweanlitterages = models.IntegerField()
    sumweanlitterages = models.IntegerField()
    arrivalentrycount = models.IntegerField()
    arrivalentryint = models.IntegerField()
    entryagecount = models.IntegerField()
    entryageint = models.IntegerField()
    totalmastitis = models.IntegerField()
    totalremastitis = models.IntegerField()
    quarter1 = models.IntegerField()
    quarter2 = models.IntegerField()
    quarter3 = models.IntegerField()
    quarter4 = models.IntegerField()
    remast1 = models.IntegerField()
    remast2 = models.IntegerField()
    remast3 = models.IntegerField()
    remast4 = models.IntegerField()
    matedfemaledays = models.IntegerField()
    nonproductivedays = models.IntegerField()
    pluriparadays = models.IntegerField()
    rowtype = models.IntegerField()
    services1 = models.IntegerField()
    summary = models.IntegerField()
    endingmaleinventory = models.IntegerField()
    mtsumfat = models.IntegerField()
    mtsummilk = models.IntegerField()
    mtsummun = models.IntegerField()
    mtsumprot = models.IntegerField()
    mtsumscc = models.IntegerField()
    mtsumsnf = models.IntegerField()
    mttests = models.IntegerField()
    mtsumdimframe = models.IntegerField()
    mtsummilkframe = models.IntegerField()
    mttestsframe = models.IntegerField()
    endingfemaleinventory = models.IntegerField()
    endingfemaleparity = models.IntegerField()
    endingunmatedfemaleinventory = models.IntegerField()
    entryfstservicedays = models.IntegerField()
    entryremovalnotserveddays = models.IntegerField()
    femaledays = models.IntegerField()
    fstserviceconceptdays = models.IntegerField()
    fstserviceremovaldays = models.IntegerField()
    lactatingdays = models.IntegerField()
    p0endingfemaleinventory = models.IntegerField()
    p0female365days = models.IntegerField()
    p0femaledays = models.IntegerField()
    p0fstserviceconceptdays = models.IntegerField()
    p0fstserviceremovaldays = models.IntegerField()
    p1femaledays = models.IntegerField()
    sumdim = models.IntegerField()
    unmatedfemaledays = models.IntegerField()
    weanfstservdays = models.IntegerField()
    weanremovalnotserveddays = models.IntegerField()
    femalestransferredin = models.IntegerField()
    entered = models.IntegerField()
    p1birthings = models.IntegerField()
    p1countbirthingages = models.IntegerField()
    p1sumbirthingages = models.IntegerField()
    birthbirthcount = models.IntegerField()
    birthbirthint = models.IntegerField()
    birthings6 = models.IntegerField()
    mummies = models.IntegerField()
    stillborn = models.IntegerField()
    sumbirthingfstserv = models.IntegerField()
    sumbirthparity = models.IntegerField()
    sumbirthweight = models.IntegerField()
    birthings = models.IntegerField()
    birthtotalweaned = models.IntegerField()
    born = models.IntegerField()
    btfemalesweaned = models.IntegerField()
    btlivebornweaned = models.IntegerField()
    countbirthingfstserv = models.IntegerField()
    countbirthweight = models.IntegerField()
    countgestationlen = models.IntegerField()
    liveborn = models.IntegerField()
    sumgestationlen = models.IntegerField()
    twinbirthings = models.IntegerField()
    countweanweight = models.IntegerField()
    femalesweaned = models.IntegerField()
    lastweaned = models.IntegerField()
    sumweanweight = models.IntegerField()
    weanings7service = models.IntegerField()
    entryfstserviceint = models.IntegerField()
    p0countagefstservice = models.IntegerField()
    p0fstserv = models.IntegerField()
    birthfstserviceint = models.IntegerField()
    entryremovalnotservedcount = models.IntegerField()
    entryremovalnotservedint = models.IntegerField()
    birthingconceptint = models.IntegerField()
    birthingconceptcount = models.IntegerField()
    conceptions = models.IntegerField()
    conceptions1 = models.IntegerField()
    countweanfstserv = models.IntegerField()
    heatconceptions = models.IntegerField()
    homospermicservices = models.IntegerField()
    multiplematings = models.IntegerField()
    p0conceptions = models.IntegerField()
    p0conceptions1 = models.IntegerField()
    p0countconceptionages = models.IntegerField()
    p0heatconceptions = models.IntegerField()
    p0pospregresult = models.IntegerField()
    p0services = models.IntegerField()
    p0sumconceptionages = models.IntegerField()
    pospregresult = models.IntegerField()
    repeatservices = models.IntegerField()
    servconception = models.IntegerField()
    services = models.IntegerField()
    services2 = models.IntegerField()
    services3 = models.IntegerField()
    servicesndaysfromwean = models.IntegerField()
    servicesai = models.IntegerField()
    servicesnatural = models.IntegerField()
    servmatings = models.IntegerField()
    weanfstserv = models.IntegerField()
    servfemalesweaned = models.IntegerField()
    servcountweanlitterages = models.IntegerField()
    servsumweanlitterages = models.IntegerField()
    servcountweanweight = models.IntegerField()
    servsumweanweight = models.IntegerField()
    servlivebornweaned = models.IntegerField()
    servparitysum = models.IntegerField()
    servremovals = models.IntegerField()
    servremovalsint = models.IntegerField()
    servabortions = models.IntegerField()
    servabortionsint = models.IntegerField()
    servbirthings = models.IntegerField()
    servborn = models.IntegerField()
    servliveborn = models.IntegerField()
    servmummies = models.IntegerField()
    servstillborn = models.IntegerField()
    servtotalweaned = models.IntegerField()
    servdeaths = models.IntegerField()
    servdeathsint = models.IntegerField()
    servfoundopen = models.IntegerField()
    servfoundopenint = models.IntegerField()
    servpdnegative = models.IntegerField()
    servpdnegativeint = models.IntegerField()
    servrepeatint = models.IntegerField()
    servrepeats = models.IntegerField()
    servunknownresult = models.IntegerField()
    pregservices = models.IntegerField()
    pregposservices = models.IntegerField()
    servicesperiodbirth = models.IntegerField()
    servicesperiodbirthadj = models.IntegerField()
    gestationdays = models.IntegerField(blank=True, null=True)
    euthanized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dmbreeding'


class Enum(models.Model):
    tableid = models.SmallIntegerField(primary_key=True)
    enumapp = models.CharField(max_length=10, blank=True, null=True)
    enumvalue = models.SmallIntegerField()
    enumname = models.CharField(max_length=30)
    displayname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'enum'
        unique_together = (('tableid', 'enumvalue'),)


class Event(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    herd = models.ForeignKey('Herd', models.DO_NOTHING)
    eventdate = models.DateField()
    evtype = models.CharField(max_length=1)
    fieldtext0 = models.CharField(max_length=20, blank=True, null=True)
    fieldtext1 = models.CharField(max_length=20, blank=True, null=True)
    fieldtext2 = models.CharField(max_length=20, blank=True, null=True)
    fieldnum0 = models.FloatField(blank=True, null=True)
    fieldnum1 = models.FloatField(blank=True, null=True)
    fieldbool0 = models.CharField(max_length=1, blank=True, null=True)
    fieldbool1 = models.CharField(max_length=1, blank=True, null=True)
    fieldubi0 = models.CharField(max_length=10, blank=True, null=True)
    fieldubi1 = models.CharField(max_length=10, blank=True, null=True)
    fieldint0 = models.IntegerField(blank=True, null=True)
    fieldint1 = models.IntegerField(blank=True, null=True)
    fieldint2 = models.IntegerField(blank=True, null=True)
    fieldint3 = models.IntegerField(blank=True, null=True)
    fieldint4 = models.IntegerField(blank=True, null=True)
    fk_pointer = models.IntegerField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    fieldint5 = models.IntegerField(blank=True, null=True)
    fieldint6 = models.IntegerField(blank=True, null=True)
    userfieldid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class Eventdeftable(models.Model):
    codifid = models.IntegerField(primary_key=True)
    enumname = models.CharField(max_length=20, blank=True, null=True)
    enumvalue = models.SmallIntegerField(unique=True, blank=True, null=True)
    predefined = models.CharField(max_length=1)
    procorder = models.SmallIntegerField(blank=True, null=True)
    evgroup = models.CharField(max_length=12)
    action = models.SmallIntegerField(blank=True, null=True)
    specific = models.CharField(max_length=1)
    female = models.CharField(max_length=1)
    male = models.CharField(max_length=1)
    offspring = models.CharField(max_length=1)
    lot = models.CharField(max_length=1)
    inir = models.CharField(max_length=5, blank=True, null=True)
    inil = models.CharField(max_length=5, blank=True, null=True)
    endr = models.CharField(max_length=5, blank=True, null=True)
    endl = models.CharField(max_length=5, blank=True, null=True)
    context = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventdeftable'


class Fielddef(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fieldposition = models.SmallIntegerField(blank=True, null=True)
    showgrid = models.CharField(max_length=1, blank=True, null=True)
    showdialog = models.CharField(max_length=1, blank=True, null=True)
    userdef = models.CharField(max_length=1, blank=True, null=True)
    virtual = models.SmallIntegerField(blank=True, null=True)
    fieldname = models.CharField(max_length=16, blank=True, null=True)
    fieldtype = models.CharField(max_length=1, blank=True, null=True)
    fieldlen = models.SmallIntegerField(blank=True, null=True)
    minval = models.FloatField(blank=True, null=True)
    maxval = models.FloatField(blank=True, null=True)
    defaultval = models.FloatField(blank=True, null=True)
    dlgwidth = models.SmallIntegerField(blank=True, null=True)
    dlglabellayout = models.SmallIntegerField(blank=True, null=True)
    dlgfieldlayout = models.SmallIntegerField(blank=True, null=True)
    lookup = models.CharField(max_length=16, blank=True, null=True)
    label = models.CharField(max_length=30, blank=True, null=True)
    showhandheld = models.CharField(max_length=1, blank=True, null=True)
    control = models.CharField(max_length=6, blank=True, null=True)
    publicname = models.CharField(max_length=16, blank=True, null=True)
    category = models.SmallIntegerField(blank=True, null=True)
    formid = models.SmallIntegerField(blank=True, null=True)
    isactive = models.CharField(max_length=1, blank=True, null=True)
    onexitid = models.CharField(max_length=16, blank=True, null=True)
    fieldfilter = models.CharField(max_length=20, blank=True, null=True)
    required = models.CharField(max_length=1, blank=True, null=True)
    inherited = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fielddef'


class Finances(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eventdate = models.DateField()
    comment = models.CharField(max_length=30, blank=True, null=True)
    import_field = models.FloatField(db_column='import', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    int0 = models.IntegerField(blank=True, null=True)
    float0 = models.FloatField(blank=True, null=True)
    float1 = models.FloatField(blank=True, null=True)
    text0 = models.CharField(max_length=10, blank=True, null=True)
    text1 = models.CharField(max_length=10, blank=True, null=True)
    date0 = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    units = models.FloatField(blank=True, null=True)
    reference = models.CharField(max_length=10, blank=True, null=True)
    ftype = models.SmallIntegerField()
    eventid = models.IntegerField(blank=True, null=True)
    row_ver = models.SmallIntegerField()
    payeeid = models.IntegerField(blank=True, null=True)
    accountid = models.IntegerField()
    inventoryid = models.IntegerField(blank=True, null=True)
    costcenter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finances'


class Herd(models.Model):
    herd_id = models.IntegerField(primary_key=True)
    RFID = models.CharField(max_length=30,null=True)
    htype = models.SmallIntegerField()
    codi = models.CharField(max_length=10)
    ubicacio = models.CharField(max_length=10, blank=True, null=True)
    dtnaixement = models.DateField(blank=True, null=True)
    dtentrada = models.DateField(blank=True, null=True)
    mare = models.CharField(max_length=10, blank=True, null=True)
    pare = models.CharField(max_length=10, blank=True, null=True)
    comentari = models.CharField(max_length=30, blank=True, null=True)
    dtbaixa = models.DateField(blank=True, null=True)
    tipusbaixa = models.SmallIntegerField(blank=True, null=True)
    estat = models.SmallIntegerField(blank=True, null=True)
    puntuacio = models.SmallIntegerField(blank=True, null=True)
    date0 = models.DateField(blank=True, null=True)
    parts = models.SmallIntegerField(blank=True, null=True)
    diagnosticfet = models.CharField(max_length=1, blank=True, null=True)
    dtrepro = models.DateField(blank=True, null=True)
    registre = models.CharField(max_length=20, blank=True, null=True)
    llibreta = models.TextField(blank=True, null=True)
    purshased = models.CharField(max_length=1, blank=True, null=True)
    conception = models.SmallIntegerField(blank=True, null=True)
    filtered = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=33, blank=True, null=True)
    pmorfo = models.SmallIntegerField(blank=True, null=True)
    qmorfo = models.SmallIntegerField(blank=True, null=True)
    iniparity = models.SmallIntegerField(blank=True, null=True)
    photo0 = models.CharField(max_length=30, blank=True, null=True)
    photo1 = models.CharField(max_length=30, blank=True, null=True)
    curservices = models.SmallIntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    sexe = models.SmallIntegerField(blank=True, null=True)
    float0 = models.FloatField(blank=True, null=True)
    float1 = models.FloatField(blank=True, null=True)
    int0 = models.IntegerField(blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    controlgenetic = models.CharField(max_length=1, blank=True, null=True)
    fk_histor_serv = models.IntegerField(blank=True, null=True)
    fk_histor_birth = models.IntegerField(blank=True, null=True)
    int1 = models.IntegerField(blank=True, null=True)
    str0 = models.CharField(max_length=10, blank=True, null=True)
    lsteventdate = models.DateField(blank=True, null=True)
    fk_treatment = models.IntegerField(blank=True, null=True)
    eid = models.CharField(max_length=30, blank=True, null=True)
    adjp1weight = models.FloatField(blank=True, null=True)
    adjp2weight = models.FloatField(blank=True, null=True)
    adjp3weight = models.FloatField(blank=True, null=True)
    lstweightage = models.SmallIntegerField(blank=True, null=True)
    pesnaixement = models.FloatField(blank=True, null=True)
    fk_last_measure = models.IntegerField(blank=True, null=True)
    lstweight = models.FloatField(blank=True, null=True)
    origintype = models.SmallIntegerField()
    integrity = models.SmallIntegerField(blank=True, null=True)
    dtalta = models.DateField(blank=True, null=True)
    fk_removal = models.IntegerField(blank=True, null=True)
    origin = models.IntegerField(blank=True, null=True)
    useraction = models.CharField(max_length=255, blank=True, null=True)
    fk_milklac = models.IntegerField(blank=True, null=True)
    userfieldid = models.IntegerField(blank=True, null=True)
    geneticsid = models.IntegerField(blank=True, null=True)
    causabaixa = models.IntegerField(blank=True, null=True)
    iid_lstpcondition1 = models.IntegerField(blank=True, null=True)
    iid_lstpcondition2 = models.IntegerField(blank=True, null=True)
    iid_lstpcondition3 = models.IntegerField(blank=True, null=True)
    iid_lstuserevent1 = models.IntegerField(blank=True, null=True)
    iid_lstuserevent2 = models.IntegerField(blank=True, null=True)
    iid_lstuserevent3 = models.IntegerField(blank=True, null=True)
    curloc1 = models.CharField(max_length=10, blank=True, null=True)
    curloc2 = models.CharField(max_length=10, blank=True, null=True)
    curloc3 = models.CharField(max_length=10, blank=True, null=True)
    lstlocationdate = models.DateField(blank=True, null=True)
    pesentrada = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    # lacstatus = models.IntegerField(blank=True, null=True)
    # reprostatus = models.IntegerField(blank=True, null=True)
    lsteventiddonordb = models.IntegerField(blank=True, null=True)
    labels = models.CharField(max_length=40, blank=True, null=True)
    iid_fsthns = models.IntegerField(blank=True, null=True)
    hnsfstservcount = models.SmallIntegerField(blank=True, null=True)
    iid_lsthns = models.IntegerField(blank=True, null=True)
    weight1 = models.FloatField(blank=True, null=True)
    weight2 = models.FloatField(blank=True, null=True)
    weight3 = models.FloatField(blank=True, null=True)
    weightdate1 = models.DateField(blank=True, null=True)
    weightdate2 = models.DateField(blank=True, null=True)
    weightdate3 = models.DateField(blank=True, null=True)
    iid_lsttreatheatind = models.IntegerField(blank=True, null=True)
    dataver = models.IntegerField(blank=True, null=True)
    weightfsthns = models.FloatField(blank=True, null=True)
    hnsdate1 = models.DateField(blank=True, null=True)
    hnsdate2 = models.DateField(blank=True, null=True)
    hnsdate3 = models.DateField(blank=True, null=True)
    arrivalweight = models.FloatField(blank=True, null=True)
    indoc = models.CharField(max_length=20, blank=True, null=True)
    txmedication = models.SmallIntegerField(blank=True, null=True)
    outdoc = models.CharField(max_length=20, blank=True, null=True)
    fk_group = models.ForeignKey('self', models.DO_NOTHING, db_column='fk_group', blank=True, null=True)
    fk_premiseid = models.ForeignKey('Premisetable', models.DO_NOTHING, db_column='fk_premiseid', blank=True, null=True)
    withdrawaldate = models.DateField(blank=True, null=True)
    tbrdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'herd'
        unique_together = (('htype', 'codi'),)

    def __str__(self):
        return str(self.herd_id)

class HerdAnimal(models.Model):
    herd = models.ForeignKey(Herd, models.DO_NOTHING)
    alelle = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'herd_animal'


class HerdFemales(models.Model):
    herd = models.ForeignKey(Herd, models.DO_NOTHING)
    lfabortions = models.SmallIntegerField(blank=True, null=True)
    lfmummies = models.SmallIntegerField(blank=True, null=True)
    lfservices = models.SmallIntegerField(blank=True, null=True)
    lfstillborn = models.SmallIntegerField(blank=True, null=True)
    heatlstdate = models.DateField(blank=True, null=True)
    servlstdate = models.DateField(blank=True, null=True)
    lfliveborn = models.SmallIntegerField(blank=True, null=True)
    lfnetadded = models.SmallIntegerField(blank=True, null=True)
    lftotalweaned = models.SmallIntegerField(blank=True, null=True)
    lflivebornlitweaned = models.SmallIntegerField(blank=True, null=True)
    lflittersweaned = models.SmallIntegerField(blank=True, null=True)
    lfnetnursed = models.SmallIntegerField(blank=True, null=True)
    lfnetfosterparity = models.SmallIntegerField(blank=True, null=True)
    statusdate = models.DateField(blank=True, null=True)
    curgroupid = models.CharField(max_length=4, blank=True, null=True)
    curgroupdate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1)
    fk_last_test = models.IntegerField(blank=True, null=True)
    fstbirthingdate = models.DateField(blank=True, null=True)
    lsteventnurseid = models.IntegerField(blank=True, null=True)
    iid_p0fstservice = models.IntegerField(blank=True, null=True)
    invlactating = models.SmallIntegerField(blank=True, null=True)
    iid_lstbirthevent = models.IntegerField(blank=True, null=True)
    lfgestationdays = models.SmallIntegerField(blank=True, null=True)
    hnsfstservno = models.SmallIntegerField(blank=True, null=True)
    iid_p0fsthns = models.IntegerField(blank=True, null=True)
    removestatuscode = models.CharField(max_length=1, blank=True, null=True)
    iid_entryevent = models.IntegerField(blank=True, null=True)
    lstoffspringid = models.CharField(max_length=10, blank=True, null=True)
    iid_arrivalservice = models.IntegerField(blank=True, null=True)
    iid_p0parity = models.IntegerField(blank=True, null=True)
    iid_p1parity = models.IntegerField(blank=True, null=True)
    lstmmdate = models.DateField(blank=True, null=True)
    lstmmmilk = models.FloatField(blank=True, null=True)
    lsttestmilk = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'herd_females'


class HerdGrowing(models.Model):
    herd = models.ForeignKey(Herd, models.DO_NOTHING, blank=True, null=True)
    fstdatein = models.DateField(blank=True, null=True)
    lstdatein = models.DateField(blank=True, null=True)
    lstdateout = models.DateField(blank=True, null=True)
    inventory = models.IntegerField(blank=True, null=True)
    recordeddeaths = models.IntegerField(blank=True, null=True)
    growingdays = models.IntegerField(blank=True, null=True)
    transferredout = models.IntegerField(blank=True, null=True)
    weighttransferredout = models.FloatField(blank=True, null=True)
    transferredin = models.IntegerField(blank=True, null=True)
    weighttransferredin = models.FloatField(blank=True, null=True)
    purchased = models.IntegerField(blank=True, null=True)
    weightpurchased = models.FloatField(blank=True, null=True)
    animalssold = models.IntegerField(blank=True, null=True)
    weightsold = models.FloatField(blank=True, null=True)
    sumindex = models.FloatField(blank=True, null=True)
    sumfat = models.FloatField(blank=True, null=True)
    sumlean = models.FloatField(blank=True, null=True)
    countsoldindex = models.IntegerField(blank=True, null=True)
    amountsold = models.FloatField(blank=True, null=True)
    countsoldfat = models.IntegerField(blank=True, null=True)
    countsoldlean = models.IntegerField(blank=True, null=True)
    weightdeaths = models.FloatField(blank=True, null=True)
    ageincount = models.IntegerField(blank=True, null=True)
    ageinsum = models.FloatField(blank=True, null=True)
    c1animalssold = models.IntegerField(blank=True, null=True)
    c1weightsold = models.FloatField(blank=True, null=True)
    c1incomesold = models.FloatField(blank=True, null=True)
    c2animalssold = models.IntegerField(blank=True, null=True)
    c2weightsold = models.FloatField(blank=True, null=True)
    c2incomesold = models.FloatField(blank=True, null=True)
    carcassweight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'herd_growing'


class Ingredientdetail(models.Model):
    ingredientdetailid = models.IntegerField(primary_key=True)
    nutrientid = models.IntegerField()
    act = models.FloatField()
    ingredientid = models.ForeignKey('Ingredienttable', models.DO_NOTHING, db_column='ingredientid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredientdetail'


class Ingredienttable(models.Model):
    codifid = models.IntegerField(primary_key=True)
    price = models.FloatField(blank=True, null=True)
    accountid = models.IntegerField(blank=True, null=True)
    feedtype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredienttable'


class Inventorytable(models.Model):
    inventoryid = models.IntegerField(primary_key=True)
    type = models.SmallIntegerField()
    itemid = models.IntegerField()
    eventid = models.IntegerField()
    invdate = models.DateField()
    units = models.FloatField()
    price = models.FloatField(blank=True, null=True)
    acumunits = models.FloatField()
    acumprice = models.FloatField()
    prevacumprice = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventorytable'
        unique_together = (('itemid', 'invdate', 'inventoryid'),)


class Locationtable(models.Model):
    locationid = models.IntegerField(primary_key=True)
    location = models.CharField(unique=True, max_length=10, blank=True, null=True)
    isactive = models.CharField(max_length=1)
    stageid = models.IntegerField()
    capacity = models.IntegerField(blank=True, null=True)
    afs = models.CharField(max_length=1, blank=True, null=True)
    eid = models.CharField(max_length=30, blank=True, null=True)
    loc1 = models.CharField(max_length=10, blank=True, null=True)
    loc2 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locationtable'


class Log(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ldate = models.DateTimeField(blank=True, null=True)
    luser = models.CharField(max_length=12, blank=True, null=True)
    ltype = models.IntegerField()
    lsubtype = models.IntegerField(blank=True, null=True)
    idkey = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    idsubkey = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class Lotinventorytable(models.Model):
    lotinventoryid = models.IntegerField(primary_key=True)
    herd = models.ForeignKey(Herd, models.DO_NOTHING)
    mindate = models.DateField()
    maxdate = models.DateField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    beginweightdate = models.DateField(blank=True, null=True)
    endweightdate = models.DateField(blank=True, null=True)
    beginweight = models.FloatField(blank=True, null=True)
    endweight = models.FloatField(blank=True, null=True)
    prevlotinventoryid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lotinventorytable'


class Nutrientconstraint(models.Model):
    nutrientconstraintid = models.IntegerField(primary_key=True)
    rationid = models.ForeignKey('Rationtable', models.DO_NOTHING, db_column='rationid')
    nutrientid = models.IntegerField()
    minvalue = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    maxvalue = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    analysis = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutrientconstraint'


class Options(models.Model):
    property = models.CharField(max_length=50)
    valor = models.CharField(max_length=254, blank=True, null=True)
    empresa = models.SmallIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'options'
        unique_together = (('empresa', 'property'),)


class Premisetable(models.Model):
    codifid = models.IntegerField(primary_key=True)
    loc1 = models.CharField(unique=True, max_length=10, blank=True, null=True)
    premisecode = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    site = models.CharField(max_length=100, blank=True, null=True)
    dbcode = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'premisetable'


class Production(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    herd = models.ForeignKey(Herd, models.DO_NOTHING)
    testdate = models.DateField()
    milk = models.FloatField()
    fat = models.FloatField(blank=True, null=True)
    prot = models.FloatField(blank=True, null=True)
    lact = models.SmallIntegerField(blank=True, null=True)
    mun = models.FloatField(blank=True, null=True)
    snf = models.FloatField(blank=True, null=True)
    testhour = models.TimeField(blank=True, null=True)
    fk_milklac = models.ForeignKey(AgParity, models.DO_NOTHING, blank=True, null=True)
    testdim = models.SmallIntegerField(blank=True, null=True)
    fk_prev_test = models.IntegerField(blank=True, null=True)
    testpos = models.SmallIntegerField(blank=True, null=True)
    scc = models.IntegerField(blank=True, null=True)
    lactose = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production'


class Rationdetail(models.Model):
    rationdetailid = models.IntegerField(primary_key=True)
    feedid = models.IntegerField()
    units = models.FloatField(blank=True, null=True)
    rationid = models.ForeignKey('Rationtable', models.DO_NOTHING, db_column='rationid', blank=True, null=True)
    minvalue = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    maxvalue = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rationdetail'


class Rationproductiontable(models.Model):
    rationproductionid = models.IntegerField(primary_key=True)
    evdate = models.DateField()
    rationid = models.IntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rationproductiontable'
        unique_together = (('evdate', 'rationproductionid'),)


class Rationtable(models.Model):
    codifid = models.IntegerField(primary_key=True)
    totalweight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rationtable'

class HeoCon(models.Model):
    name = models.IntegerField(primary_key=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'HeoCon'

class Targetdetailtable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    codifid = models.ForeignKey(Codiftable, models.DO_NOTHING, db_column='codifid', blank=True, null=True)
    caption = models.CharField(max_length=30, blank=True, null=True)
    rowid = models.IntegerField(blank=True, null=True)
    target = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'targetdetailtable'


class Treatmenttable(models.Model):
    codifid = models.IntegerField(primary_key=True)
    application = models.SmallIntegerField()
    amount = models.FloatField(blank=True, null=True)
    unitsid = models.SmallIntegerField(blank=True, null=True)
    route = models.SmallIntegerField(blank=True, null=True)
    userevent = models.SmallIntegerField(blank=True, null=True)
    withdrawal = models.SmallIntegerField(blank=True, null=True)
    lastreceipt = models.CharField(max_length=20, blank=True, null=True)
    treattype = models.IntegerField(blank=True, null=True)
    precondition = models.IntegerField(blank=True, null=True)
    treatgroup = models.SmallIntegerField(blank=True, null=True)
    triggerevent = models.SmallIntegerField(blank=True, null=True)
    triggerdays = models.SmallIntegerField(blank=True, null=True)
    mintriggerdays = models.SmallIntegerField(blank=True, null=True)
    maxtriggerdays = models.SmallIntegerField(blank=True, null=True)
    repeatdays = models.CharField(max_length=60, blank=True, null=True)
    prevtreat = models.IntegerField(blank=True, null=True)
    minprevtreatdays = models.SmallIntegerField(blank=True, null=True)
    maxprevtreatdays = models.SmallIntegerField(blank=True, null=True)
    begindate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treatmenttable'


class Treball(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evtype = models.CharField(max_length=1)
    eventdate = models.DateField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    animal = models.CharField(max_length=30, blank=True, null=True)
    missatge = models.CharField(max_length=255, blank=True, null=True)
    fieldtext0 = models.CharField(max_length=20, blank=True, null=True)
    fieldtext1 = models.CharField(max_length=20, blank=True, null=True)
    fieldtext2 = models.CharField(max_length=20, blank=True, null=True)
    fieldnum0 = models.FloatField(blank=True, null=True)
    fieldnum1 = models.FloatField(blank=True, null=True)
    fieldbool0 = models.CharField(max_length=1, blank=True, null=True)
    fieldbool1 = models.CharField(max_length=1, blank=True, null=True)
    fieldubi0 = models.CharField(max_length=10, blank=True, null=True)
    fieldubi1 = models.CharField(max_length=10, blank=True, null=True)
    fieldint0 = models.IntegerField(blank=True, null=True)
    fieldint1 = models.IntegerField(blank=True, null=True)
    fieldint2 = models.IntegerField(blank=True, null=True)
    fieldint3 = models.IntegerField(blank=True, null=True)
    fieldint4 = models.IntegerField(blank=True, null=True)
    htype = models.SmallIntegerField()
    comment = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    fieldint5 = models.IntegerField(blank=True, null=True)
    fieldint6 = models.IntegerField(blank=True, null=True)
    userfieldid = models.IntegerField(blank=True, null=True)
    owner = models.CharField(max_length=30, blank=True, null=True)
    refid = models.IntegerField(blank=True, null=True)
    idby = models.SmallIntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treball'


class Userfieldtable(models.Model):
    userfieldid = models.IntegerField(primary_key=True)
    uftype = models.IntegerField()
    text1 = models.CharField(max_length=64, blank=True, null=True)
    text2 = models.CharField(max_length=64, blank=True, null=True)
    text3 = models.CharField(max_length=64, blank=True, null=True)
    text4 = models.CharField(max_length=64, blank=True, null=True)
    text5 = models.CharField(max_length=64, blank=True, null=True)
    text6 = models.CharField(max_length=64, blank=True, null=True)
    text7 = models.CharField(max_length=64, blank=True, null=True)
    text8 = models.CharField(max_length=64, blank=True, null=True)
    text9 = models.CharField(max_length=64, blank=True, null=True)
    text10 = models.CharField(max_length=64, blank=True, null=True)
    text11 = models.CharField(max_length=64, blank=True, null=True)
    text12 = models.CharField(max_length=64, blank=True, null=True)
    text13 = models.CharField(max_length=64, blank=True, null=True)
    text14 = models.CharField(max_length=64, blank=True, null=True)
    text15 = models.CharField(max_length=64, blank=True, null=True)
    text16 = models.CharField(max_length=64, blank=True, null=True)
    decimal1 = models.FloatField(blank=True, null=True)
    decimal2 = models.FloatField(blank=True, null=True)
    decimal3 = models.FloatField(blank=True, null=True)
    decimal4 = models.FloatField(blank=True, null=True)
    bool1 = models.CharField(max_length=1, blank=True, null=True)
    bool2 = models.CharField(max_length=1, blank=True, null=True)
    bool3 = models.CharField(max_length=1, blank=True, null=True)
    bool4 = models.CharField(max_length=1, blank=True, null=True)
    datetime1 = models.DateTimeField(blank=True, null=True)
    datetime2 = models.DateTimeField(blank=True, null=True)
    datetime3 = models.DateTimeField(blank=True, null=True)
    datetime4 = models.DateTimeField(blank=True, null=True)
    decimal5 = models.FloatField(blank=True, null=True)
    decimal6 = models.FloatField(blank=True, null=True)
    decimal7 = models.FloatField(blank=True, null=True)
    decimal8 = models.FloatField(blank=True, null=True)
    decimal9 = models.FloatField(blank=True, null=True)
    decimal10 = models.FloatField(blank=True, null=True)
    decimal11 = models.FloatField(blank=True, null=True)
    decimal12 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userfieldtable'


class Usertable(models.Model):
    codifid = models.IntegerField(primary_key=True)
    productivereports = models.CharField(max_length=1, blank=True, null=True)
    financialreports = models.CharField(max_length=1, blank=True, null=True)
    dataentry = models.CharField(max_length=1, blank=True, null=True)
    editoptions = models.CharField(max_length=1, blank=True, null=True)
    editreports = models.CharField(max_length=1, blank=True, null=True)
    deleterecords = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usertable'
